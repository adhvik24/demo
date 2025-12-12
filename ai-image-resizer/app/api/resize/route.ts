import { NextRequest, NextResponse } from "next/server";
import sharp from "sharp";

export async function POST(request: NextRequest) {
  const startTime = Date.now();
  
  try {
    const formData = await request.formData();
    const image = formData.get("image") as File;
    const optionsStr = formData.get("options") as string;

    if (!image) {
      return NextResponse.json(
        { error: "No image provided" },
        { status: 400 }
      );
    }

    const options = JSON.parse(optionsStr);
    const buffer = Buffer.from(await image.arrayBuffer());
    const originalSize = buffer.length;

    let sharpInstance = sharp(buffer);

    // Get image metadata for smart processing
    const metadata = await sharpInstance.metadata();

    // Apply resize with specified options
    const resizeOptions: sharp.ResizeOptions = {
      width: options.width,
      height: options.height,
      fit: options.fit,
    };

    // For cover mode, use attention strategy for AI-powered smart cropping
    if (options.fit === "cover") {
      resizeOptions.position = sharp.strategy.attention;
    }

    sharpInstance = sharpInstance.resize(resizeOptions);

    // Apply format conversion and quality settings
    let outputBuffer: Buffer;

    switch (options.format) {
      case "jpeg":
        outputBuffer = await sharpInstance
          .jpeg({ quality: options.quality, mozjpeg: true })
          .toBuffer();
        break;
      case "png":
        outputBuffer = await sharpInstance
          .png({
            quality: options.quality,
            compressionLevel: Math.floor((100 - options.quality) / 10),
          })
          .toBuffer();
        break;
      case "webp":
        outputBuffer = await sharpInstance
          .webp({ quality: options.quality })
          .toBuffer();
        break;
      default:
        outputBuffer = await sharpInstance
          .jpeg({ quality: options.quality })
          .toBuffer();
    }

    const processingTime = Date.now() - startTime;
    const processedSize = outputBuffer.length;

    // Track analytics asynchronously (don't wait for it)
    fetch(`${request.nextUrl.origin}/api/analytics`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        originalSize,
        processedSize,
        format: options.format,
        quality: options.quality,
        width: options.width,
        height: options.height,
        fit: options.fit,
        processingTime,
      }),
    }).catch((err) => console.error("Failed to track analytics:", err));

    // Return the processed image
    return new NextResponse(outputBuffer as unknown as BodyInit, {
      headers: {
        "Content-Type": `image/${options.format}`,
        "Content-Disposition": `attachment; filename="resized.${options.format}"`,
      },
    });
  } catch (error) {
    console.error("Image processing error:", error);
    return NextResponse.json(
      { error: "Failed to process image" },
      { status: 500 }
    );
  }
}
