"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

export default function Navigation() {
  const pathname = usePathname();

  return (
    <nav className="bg-white dark:bg-gray-800 shadow-md mb-8 rounded-2xl">
      <div className="max-w-7xl mx-auto px-6 py-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-8">
            <Link
              href="/"
              className="text-2xl font-bold text-blue-600 dark:text-blue-400"
            >
              AI Image Resizer
            </Link>
            <div className="hidden md:flex space-x-6">
              <Link
                href="/"
                className={`font-medium transition-colors ${
                  pathname === "/"
                    ? "text-blue-600 dark:text-blue-400"
                    : "text-gray-600 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400"
                }`}
              >
                Home
              </Link>
              <Link
                href="/payment"
                className={`font-medium transition-colors ${
                  pathname === "/payment"
                    ? "text-blue-600 dark:text-blue-400"
                    : "text-gray-600 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400"
                }`}
              >
                Pricing
              </Link>
            </div>
          </div>
          <Link
            href="/payment"
            className="bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-6 rounded-lg transition-colors duration-200"
          >
            Upgrade
          </Link>
        </div>
      </div>
    </nav>
  );
}
