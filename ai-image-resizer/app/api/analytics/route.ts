import { NextRequest, NextResponse } from "next/server";
import fs from "fs/promises";
import path from "path";

const ANALYTICS_FILE = path.join(process.cwd(), "analytics-data.json");

interface AnalyticsEntry {
  timestamp: string;
  originalSize: number;
  processedSize: number;
  format: string;
  quality: number;
  width: number;
  height: number;
  fit: string;
  processingTime: number;
  compressionRatio: string;
}

async function readAnalytics(): Promise<AnalyticsEntry[]> {
  try {
    const data = await fs.readFile(ANALYTICS_FILE, "utf-8");
    return JSON.parse(data);
  } catch (error) {
    return [];
  }
}

async function writeAnalytics(data: AnalyticsEntry[]): Promise<void> {
  await fs.writeFile(ANALYTICS_FILE, JSON.stringify(data, null, 2));
}

export async function POST(request: NextRequest) {
  try {
    const data = await request.json();

    const analyticsEntry: AnalyticsEntry = {
      timestamp: new Date().toISOString(),
      originalSize: data.originalSize,
      processedSize: data.processedSize,
      format: data.format,
      quality: data.quality,
      width: data.width,
      height: data.height,
      fit: data.fit,
      processingTime: data.processingTime,
      compressionRatio:
        data.originalSize > 0
          ? (
              ((data.originalSize - data.processedSize) / data.originalSize) *
              100
            ).toFixed(2)
          : "0",
    };

    const analytics = await readAnalytics();
    analytics.push(analyticsEntry);
    await writeAnalytics(analytics);

    return NextResponse.json({ success: true, id: analyticsEntry });
  } catch (error) {
    console.error("Analytics storage error:", error);
    return NextResponse.json(
      { error: "Failed to store analytics" },
      { status: 500 }
    );
  }
}

export async function GET(request: NextRequest) {
  try {
    const { searchParams } = new URL(request.url);
    const days = parseInt(searchParams.get("days") || "30");

    const analytics = await readAnalytics();

    const startDate = new Date();
    startDate.setDate(startDate.getDate() - days);

    const filteredAnalytics = analytics.filter(
      (item) => new Date(item.timestamp) >= startDate
    );

    // Calculate aggregated statistics
    const totalProcessed = filteredAnalytics.length;
    const totalOriginalSize = filteredAnalytics.reduce(
      (sum, item) => sum + (item.originalSize || 0),
      0
    );
    const totalProcessedSize = filteredAnalytics.reduce(
      (sum, item) => sum + (item.processedSize || 0),
      0
    );
    const totalSaved = totalOriginalSize - totalProcessedSize;
    const avgProcessingTime =
      filteredAnalytics.length > 0
        ? filteredAnalytics.reduce(
            (sum, item) => sum + (item.processingTime || 0),
            0
          ) / filteredAnalytics.length
        : 0;

    // Format distribution
    const formatDistribution = filteredAnalytics.reduce(
      (acc: Record<string, number>, item) => {
        acc[item.format] = (acc[item.format] || 0) + 1;
        return acc;
      },
      {}
    );

    // Daily processing counts
    const dailyStats = filteredAnalytics.reduce(
      (acc: Record<string, number>, item) => {
        const date = new Date(item.timestamp).toISOString().split("T")[0];
        acc[date] = (acc[date] || 0) + 1;
        return acc;
      },
      {}
    );

    return NextResponse.json({
      summary: {
        totalProcessed,
        totalOriginalSize,
        totalProcessedSize,
        totalSaved,
        avgProcessingTime: avgProcessingTime.toFixed(2),
        avgCompressionRatio:
          totalOriginalSize > 0
            ? ((totalSaved / totalOriginalSize) * 100).toFixed(2)
            : "0",
      },
      formatDistribution,
      dailyStats,
      recentProcessing: filteredAnalytics.slice(-10).reverse(),
    });
  } catch (error) {
    console.error("Analytics retrieval error:", error);
    return NextResponse.json(
      { error: "Failed to retrieve analytics" },
      { status: 500 }
    );
  }
}
