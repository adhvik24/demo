"use client";

import { useState } from "react";
import Link from "next/link";

interface PricingTier {
  name: string;
  price: number;
  yearlyPrice: number;
  description: string;
  features: string[];
  highlighted?: boolean;
  cta: string;
}

interface FAQ {
  question: string;
  answer: string;
}

interface Testimonial {
  name: string;
  role: string;
  company: string;
  content: string;
  rating: number;
}

export default function PricingPage() {
  const [isYearly, setIsYearly] = useState(false);
  const [openFaqIndex, setOpenFaqIndex] = useState<number | null>(null);

  const pricingTiers: PricingTier[] = [
    {
      name: "Basic",
      price: 9,
      yearlyPrice: 90,
      description: "Perfect for individuals and small projects",
      features: [
        "Up to 100 images per month",
        "Basic resize and optimization",
        "JPEG, PNG, WebP formats",
        "Standard processing speed",
        "Email support",
        "7-day money-back guarantee",
      ],
      cta: "Start Basic",
    },
    {
      name: "Pro",
      price: 29,
      yearlyPrice: 290,
      description: "Ideal for professionals and growing businesses",
      features: [
        "Up to 1,000 images per month",
        "AI-powered smart cropping",
        "All image formats supported",
        "Priority processing speed",
        "Advanced optimization tools",
        "API access included",
        "Priority email & chat support",
        "30-day money-back guarantee",
      ],
      highlighted: true,
      cta: "Start Pro",
    },
    {
      name: "Enterprise",
      price: 99,
      yearlyPrice: 990,
      description: "For large teams and high-volume needs",
      features: [
        "Unlimited images per month",
        "Full AI suite with custom models",
        "Batch processing capabilities",
        "Dedicated processing servers",
        "Custom integrations & webhooks",
        "White-label options",
        "Dedicated account manager",
        "24/7 priority support",
        "Custom SLA agreements",
      ],
      cta: "Contact Sales",
    },
  ];

  const features = [
    {
      title: "AI-Powered Smart Cropping",
      description:
        "Our advanced AI automatically detects and preserves the most important parts of your images when resizing.",
    },
    {
      title: "Lightning Fast Processing",
      description:
        "Process thousands of images in minutes with our optimized cloud infrastructure and parallel processing.",
    },
    {
      title: "Format Flexibility",
      description:
        "Support for all major image formats including JPEG, PNG, WebP, AVIF, and more with automatic optimization.",
    },
    {
      title: "API Integration",
      description:
        "Seamlessly integrate our service into your workflow with our comprehensive RESTful API and SDKs.",
    },
    {
      title: "Batch Processing",
      description:
        "Upload and process multiple images simultaneously with our powerful batch processing capabilities.",
    },
    {
      title: "Secure & Private",
      description:
        "Your images are encrypted in transit and at rest, and automatically deleted after processing.",
    },
  ];

  const testimonials: Testimonial[] = [
    {
      name: "Sarah Johnson",
      role: "Creative Director",
      company: "DesignHub Studio",
      content:
        "This tool has saved us countless hours. The AI smart cropping is incredibly accurate and the batch processing is a game-changer for our workflow.",
      rating: 5,
    },
    {
      name: "Michael Chen",
      role: "E-commerce Manager",
      company: "ShopFlow Inc",
      content:
        "We process thousands of product images monthly. The API integration was seamless and the quality is consistently excellent. Highly recommend!",
      rating: 5,
    },
    {
      name: "Emily Rodriguez",
      role: "Marketing Lead",
      company: "GrowthTech",
      content:
        "The Pro plan is perfect for our team. Fast processing, great support, and the pricing is very reasonable for the value we get.",
      rating: 5,
    },
  ];

  const faqs: FAQ[] = [
    {
      question: "How does the billing work?",
      answer:
        "You can choose between monthly or yearly billing. Yearly plans save you 17% compared to monthly. All plans include a money-back guarantee and you can cancel anytime.",
    },
    {
      question: "What payment methods do you accept?",
      answer:
        "We accept all major credit cards (Visa, MasterCard, American Express), PayPal, and for Enterprise plans, we also support wire transfers and purchase orders.",
    },
    {
      question: "Can I upgrade or downgrade my plan?",
      answer:
        "Yes! You can upgrade or downgrade your plan at any time. When upgrading, you'll be charged a prorated amount. When downgrading, the change takes effect at the start of your next billing cycle.",
    },
    {
      question: "What happens if I exceed my monthly limit?",
      answer:
        "If you approach your monthly limit, we'll send you a notification. You can either upgrade your plan or purchase additional image credits. Your service won't be interrupted.",
    },
    {
      question: "Is there a free trial available?",
      answer:
        "Yes! All new users get a 14-day free trial with access to Pro features. No credit card required to start your trial.",
    },
    {
      question: "How secure is my data?",
      answer:
        "We take security seriously. All images are encrypted in transit (TLS 1.3) and at rest (AES-256). Images are automatically deleted from our servers after 24 hours. We're SOC 2 Type II certified.",
    },
    {
      question: "Do you offer refunds?",
      answer:
        "Yes! We offer a 7-day money-back guarantee for Basic plans and 30-day for Pro and Enterprise plans. If you're not satisfied, contact us for a full refund.",
    },
    {
      question: "Can I get a custom plan for my specific needs?",
      answer:
        "Absolutely! For Enterprise customers, we can create custom plans tailored to your specific requirements. Contact our sales team to discuss your needs.",
    },
  ];

  const toggleFaq = (index: number) => {
    setOpenFaqIndex(openFaqIndex === index ? null : index);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-indigo-50 dark:from-gray-900 dark:via-gray-800 dark:to-gray-900">
      {/* Hero Section */}
      <section className="relative overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-br from-blue-600/10 to-indigo-600/10 dark:from-blue-600/5 dark:to-indigo-600/5"></div>
        <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 sm:py-28">
          <div className="text-center">
            <h1 className="text-5xl sm:text-6xl lg:text-7xl font-bold text-gray-900 dark:text-white mb-6 leading-tight">
              Simple, Transparent
              <span className="block text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-indigo-600 dark:from-blue-400 dark:to-indigo-400">
                Pricing
              </span>
            </h1>
            <p className="text-xl sm:text-2xl text-gray-600 dark:text-gray-300 mb-8 max-w-3xl mx-auto">
              Choose the perfect plan for your image processing needs. All plans
              include our AI-powered features and world-class support.
            </p>
            <div className="flex items-center justify-center gap-4 mb-12">
              <span
                className={`text-lg font-medium ${
                  !isYearly
                    ? "text-gray-900 dark:text-white"
                    : "text-gray-500 dark:text-gray-400"
                }`}
              >
                Monthly
              </span>
              <button
                onClick={() => setIsYearly(!isYearly)}
                className="relative inline-flex h-8 w-16 items-center rounded-full bg-gray-300 dark:bg-gray-600 transition-colors focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
                aria-label="Toggle yearly billing"
              >
                <span
                  className={`inline-block h-6 w-6 transform rounded-full bg-white transition-transform ${
                    isYearly ? "translate-x-9" : "translate-x-1"
                  }`}
                />
              </button>
              <span
                className={`text-lg font-medium ${
                  isYearly
                    ? "text-gray-900 dark:text-white"
                    : "text-gray-500 dark:text-gray-400"
                }`}
              >
                Yearly
              </span>
              <span className="ml-2 inline-flex items-center rounded-full bg-green-100 dark:bg-green-900/30 px-3 py-1 text-sm font-medium text-green-800 dark:text-green-300">
                Save 17%
              </span>
            </div>
          </div>
        </div>
      </section>

      {/* Pricing Tiers */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {pricingTiers.map((tier, index) => (
            <div
              key={index}
              className={`relative rounded-2xl ${
                tier.highlighted
                  ? "bg-gradient-to-br from-blue-600 to-indigo-600 shadow-2xl scale-105 md:scale-110"
                  : "bg-white dark:bg-gray-800 shadow-xl"
              } p-8 transition-transform hover:scale-105`}
            >
              {tier.highlighted && (
                <div className="absolute -top-5 left-1/2 transform -translate-x-1/2">
                  <span className="inline-flex items-center rounded-full bg-yellow-400 px-4 py-1 text-sm font-bold text-gray-900">
                    Most Popular
                  </span>
                </div>
              )}

              <div className="text-center mb-8">
                <h3
                  className={`text-2xl font-bold mb-2 ${
                    tier.highlighted
                      ? "text-white"
                      : "text-gray-900 dark:text-white"
                  }`}
                >
                  {tier.name}
                </h3>
                <p
                  className={`text-sm ${
                    tier.highlighted
                      ? "text-blue-100"
                      : "text-gray-600 dark:text-gray-400"
                  }`}
                >
                  {tier.description}
                </p>
              </div>

              <div className="text-center mb-8">
                <div className="flex items-baseline justify-center">
                  <span
                    className={`text-5xl font-bold ${
                      tier.highlighted
                        ? "text-white"
                        : "text-gray-900 dark:text-white"
                    }`}
                  >
                    ${isYearly ? tier.yearlyPrice : tier.price}
                  </span>
                  <span
                    className={`ml-2 text-lg ${
                      tier.highlighted
                        ? "text-blue-100"
                        : "text-gray-600 dark:text-gray-400"
                    }`}
                  >
                    /{isYearly ? "year" : "month"}
                  </span>
                </div>
                {isYearly && (
                  <p
                    className={`mt-2 text-sm ${
                      tier.highlighted
                        ? "text-blue-100"
                        : "text-gray-500 dark:text-gray-400"
                    }`}
                  >
                    ${(tier.yearlyPrice / 12).toFixed(2)} per month
                  </p>
                )}
              </div>

              <ul className="space-y-4 mb-8">
                {tier.features.map((feature, featureIndex) => (
                  <li key={featureIndex} className="flex items-start">
                    <span
                      className={`mr-3 mt-1 ${
                        tier.highlighted ? "text-blue-200" : "text-green-500"
                      }`}
                    >
                      ✓
                    </span>
                    <span
                      className={`text-sm ${
                        tier.highlighted
                          ? "text-white"
                          : "text-gray-700 dark:text-gray-300"
                      }`}
                    >
                      {feature}
                    </span>
                  </li>
                ))}
              </ul>

              <button
                className={`w-full py-4 px-6 rounded-xl font-semibold text-lg transition-all ${
                  tier.highlighted
                    ? "bg-white text-blue-600 hover:bg-gray-100 shadow-lg"
                    : "bg-blue-600 text-white hover:bg-blue-700 dark:bg-blue-500 dark:hover:bg-blue-600"
                }`}
              >
                {tier.cta}
              </button>
            </div>
          ))}
        </div>

        <div className="mt-12 text-center">
          <p className="text-gray-600 dark:text-gray-400">
            All plans include SSL encryption, automatic backups, and 99.9%
            uptime SLA
          </p>
        </div>
      </section>

      {/* Features Section */}
      <section className="bg-white dark:bg-gray-800 py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-gray-900 dark:text-white mb-4">
              Powerful Features for Every Plan
            </h2>
            <p className="text-xl text-gray-600 dark:text-gray-300 max-w-3xl mx-auto">
              Get access to industry-leading image processing technology with
              every subscription
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {features.map((feature, index) => (
              <div
                key={index}
                className="bg-gradient-to-br from-gray-50 to-gray-100 dark:from-gray-700 dark:to-gray-800 rounded-xl p-6 hover:shadow-lg transition-shadow"
              >
                <div className="w-12 h-12 bg-blue-600 dark:bg-blue-500 rounded-lg flex items-center justify-center mb-4 text-2xl text-white">
                  {index + 1}
                </div>
                <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-3">
                  {feature.title}
                </h3>
                <p className="text-gray-600 dark:text-gray-300">
                  {feature.description}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Testimonials Section */}
      <section className="py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-gray-900 dark:text-white mb-4">
              Loved by Thousands of Users
            </h2>
            <p className="text-xl text-gray-600 dark:text-gray-300">
              See what our customers have to say about their experience
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {testimonials.map((testimonial, index) => (
              <div
                key={index}
                className="bg-white dark:bg-gray-800 rounded-xl p-8 shadow-lg hover:shadow-xl transition-shadow"
              >
                <div className="flex mb-4">
                  {[...Array(testimonial.rating)].map((_, i) => (
                    <span key={i} className="text-yellow-400 text-xl">
                      ★
                    </span>
                  ))}
                </div>
                <p className="text-gray-700 dark:text-gray-300 mb-6 italic">
                  &quot;{testimonial.content}&quot;
                </p>
                <div className="border-t border-gray-200 dark:border-gray-700 pt-4">
                  <p className="font-semibold text-gray-900 dark:text-white">
                    {testimonial.name}
                  </p>
                  <p className="text-sm text-gray-600 dark:text-gray-400">
                    {testimonial.role}
                  </p>
                  <p className="text-sm text-blue-600 dark:text-blue-400">
                    {testimonial.company}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* FAQ Section */}
      <section className="bg-white dark:bg-gray-800 py-20">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-gray-900 dark:text-white mb-4">
              Frequently Asked Questions
            </h2>
            <p className="text-xl text-gray-600 dark:text-gray-300">
              Everything you need to know about our pricing and plans
            </p>
          </div>

          <div className="space-y-4">
            {faqs.map((faq, index) => (
              <div
                key={index}
                className="bg-gray-50 dark:bg-gray-700 rounded-xl overflow-hidden"
              >
                <button
                  onClick={() => toggleFaq(index)}
                  className="w-full px-6 py-5 text-left flex items-center justify-between hover:bg-gray-100 dark:hover:bg-gray-600 transition-colors"
                >
                  <span className="font-semibold text-lg text-gray-900 dark:text-white pr-8">
                    {faq.question}
                  </span>
                  <span
                    className={`text-2xl text-blue-600 dark:text-blue-400 transform transition-transform ${
                      openFaqIndex === index ? "rotate-180" : ""
                    }`}
                  >
                    ↓
                  </span>
                </button>
                {openFaqIndex === index && (
                  <div className="px-6 pb-5">
                    <p className="text-gray-700 dark:text-gray-300">
                      {faq.answer}
                    </p>
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="bg-gradient-to-r from-blue-600 to-indigo-600 rounded-3xl p-12 text-center shadow-2xl">
            <h2 className="text-4xl font-bold text-white mb-4">
              Ready to Get Started?
            </h2>
            <p className="text-xl text-blue-100 mb-8">
              Join thousands of satisfied customers and start processing images
              smarter today
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <button className="bg-white text-blue-600 px-8 py-4 rounded-xl font-semibold text-lg hover:bg-gray-100 transition-colors shadow-lg">
                Start Free Trial
              </button>
              <button className="bg-blue-700 text-white px-8 py-4 rounded-xl font-semibold text-lg hover:bg-blue-800 transition-colors border-2 border-white">
                Contact Sales
              </button>
            </div>
            <p className="text-blue-100 mt-6 text-sm">
              No credit card required • 14-day free trial • Cancel anytime
            </p>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 dark:bg-black text-white py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-12 mb-12">
            <div>
              <h3 className="text-2xl font-bold mb-4">AI Image Resizer</h3>
              <p className="text-gray-400 mb-4">
                Smart, AI-powered image resizing and optimization for modern
                workflows.
              </p>
            </div>

            <div>
              <h4 className="font-semibold text-lg mb-4">Product</h4>
              <ul className="space-y-2">
                <li>
                  <Link
                    href="/"
                    className="text-gray-400 hover:text-white transition-colors"
                  >
                    Features
                  </Link>
                </li>
                <li>
                  <Link
                    href="/pricing"
                    className="text-gray-400 hover:text-white transition-colors"
                  >
                    Pricing
                  </Link>
                </li>
                <li>
                  <a
                    href="#"
                    className="text-gray-400 hover:text-white transition-colors"
                  >
                    API Documentation
                  </a>
                </li>
                <li>
                  <a
                    href="#"
                    className="text-gray-400 hover:text-white transition-colors"
                  >
                    Integrations
                  </a>
                </li>
              </ul>
            </div>

            <div>
              <h4 className="font-semibold text-lg mb-4">Company</h4>
              <ul className="space-y-2">
                <li>
                  <a
                    href="#"
                    className="text-gray-400 hover:text-white transition-colors"
                  >
                    About Us
                  </a>
                </li>
                <li>
                  <a
                    href="#"
                    className="text-gray-400 hover:text-white transition-colors"
                  >
                    Blog
                  </a>
                </li>
                <li>
                  <a
                    href="#"
                    className="text-gray-400 hover:text-white transition-colors"
                  >
                    Careers
                  </a>
                </li>
                <li>
                  <a
                    href="#"
                    className="text-gray-400 hover:text-white transition-colors"
                  >
                    Contact
                  </a>
                </li>
              </ul>
            </div>

            <div>
              <h4 className="font-semibold text-lg mb-4">Support</h4>
              <ul className="space-y-2">
                <li>
                  <a
                    href="#"
                    className="text-gray-400 hover:text-white transition-colors"
                  >
                    Help Center
                  </a>
                </li>
                <li>
                  <a
                    href="#"
                    className="text-gray-400 hover:text-white transition-colors"
                  >
                    Privacy Policy
                  </a>
                </li>
                <li>
                  <a
                    href="#"
                    className="text-gray-400 hover:text-white transition-colors"
                  >
                    Terms of Service
                  </a>
                </li>
                <li>
                  <a
                    href="mailto:support@aiimageresizer.com"
                    className="text-gray-400 hover:text-white transition-colors"
                  >
                    support@aiimageresizer.com
                  </a>
                </li>
              </ul>
            </div>
          </div>

          <div className="border-t border-gray-800 pt-8">
            <div className="flex flex-col md:flex-row justify-between items-center">
              <p className="text-gray-400 text-sm mb-4 md:mb-0">
                © 2025 AI Image Resizer. All rights reserved.
              </p>
              <div className="flex gap-6">
                <a
                  href="#"
                  className="text-gray-400 hover:text-white transition-colors"
                >
                  Twitter
                </a>
                <a
                  href="#"
                  className="text-gray-400 hover:text-white transition-colors"
                >
                  LinkedIn
                </a>
                <a
                  href="#"
                  className="text-gray-400 hover:text-white transition-colors"
                >
                  GitHub
                </a>
              </div>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}
