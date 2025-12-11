"use client";

import { useState } from "react";
import Link from "next/link";

interface PaymentFormData {
  cardNumber: string;
  cardName: string;
  expiryDate: string;
  cvv: string;
  email: string;
  billingAddress: string;
  city: string;
  zipCode: string;
  country: string;
}

interface PricingPlan {
  name: string;
  price: number;
  period: string;
  features: string[];
  popular?: boolean;
}

export default function PaymentPage() {
  const [selectedPlan, setSelectedPlan] = useState<string>("pro");
  const [paymentMethod, setPaymentMethod] = useState<"card" | "paypal">("card");
  const [isProcessing, setIsProcessing] = useState(false);
  const [formData, setFormData] = useState<PaymentFormData>({
    cardNumber: "",
    cardName: "",
    expiryDate: "",
    cvv: "",
    email: "",
    billingAddress: "",
    city: "",
    zipCode: "",
    country: "",
  });
  const [errors, setErrors] = useState<Partial<PaymentFormData>>({});

  const pricingPlans: PricingPlan[] = [
    {
      name: "Basic",
      price: 9.99,
      period: "month",
      features: [
        "100 images per month",
        "Basic resize options",
        "JPEG & PNG formats",
        "Email support",
      ],
    },
    {
      name: "Pro",
      price: 24.99,
      period: "month",
      features: [
        "Unlimited images",
        "AI Smart Cropping",
        "All formats (JPEG, PNG, WebP)",
        "Priority support",
        "Batch processing",
        "API access",
      ],
      popular: true,
    },
    {
      name: "Enterprise",
      price: 99.99,
      period: "month",
      features: [
        "Everything in Pro",
        "Custom integrations",
        "Dedicated support",
        "SLA guarantee",
        "Advanced analytics",
        "White-label option",
      ],
    },
  ];

  const validateForm = (): boolean => {
    const newErrors: Partial<PaymentFormData> = {};

    if (paymentMethod === "card") {
      if (!formData.cardNumber || formData.cardNumber.replace(/\s/g, "").length !== 16) {
        newErrors.cardNumber = "Please enter a valid 16-digit card number";
      }
      if (!formData.cardName || formData.cardName.trim().length < 3) {
        newErrors.cardName = "Please enter the cardholder name";
      }
      if (!formData.expiryDate || !/^\d{2}\/\d{2}$/.test(formData.expiryDate)) {
        newErrors.expiryDate = "Please enter expiry date (MM/YY)";
      }
      if (!formData.cvv || formData.cvv.length !== 3) {
        newErrors.cvv = "Please enter a valid 3-digit CVV";
      }
    }

    if (!formData.email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
      newErrors.email = "Please enter a valid email address";
    }
    if (!formData.billingAddress || formData.billingAddress.trim().length < 5) {
      newErrors.billingAddress = "Please enter your billing address";
    }
    if (!formData.city || formData.city.trim().length < 2) {
      newErrors.city = "Please enter your city";
    }
    if (!formData.zipCode || formData.zipCode.trim().length < 3) {
      newErrors.zipCode = "Please enter your ZIP code";
    }
    if (!formData.country || formData.country.trim().length < 2) {
      newErrors.country = "Please enter your country";
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleInputChange = (field: keyof PaymentFormData, value: string) => {
    setFormData({ ...formData, [field]: value });
    if (errors[field]) {
      setErrors({ ...errors, [field]: undefined });
    }
  };

  const formatCardNumber = (value: string) => {
    const cleaned = value.replace(/\s/g, "");
    const formatted = cleaned.match(/.{1,4}/g)?.join(" ") || cleaned;
    return formatted.slice(0, 19);
  };

  const formatExpiryDate = (value: string) => {
    const cleaned = value.replace(/\D/g, "");
    if (cleaned.length >= 2) {
      return cleaned.slice(0, 2) + "/" + cleaned.slice(2, 4);
    }
    return cleaned;
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!validateForm()) {
      return;
    }

    setIsProcessing(true);

    setTimeout(() => {
      setIsProcessing(false);
      alert(`Payment successful! Welcome to the ${selectedPlan} plan.`);
    }, 2000);
  };

  const selectedPlanDetails = pricingPlans.find(
    (plan) => plan.name.toLowerCase() === selectedPlan
  );

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 dark:from-gray-900 dark:to-gray-800 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl mx-auto">
        {/* Header with Navigation */}
        <div className="mb-8">
          <Link
            href="/"
            className="inline-flex items-center text-blue-600 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 font-medium"
          >
            ← Back to Home
          </Link>
        </div>

        <div className="text-center mb-12">
          <h1 className="text-5xl font-bold text-gray-900 dark:text-white mb-4">
            Choose Your Plan
          </h1>
          <p className="text-xl text-gray-600 dark:text-gray-300">
            Unlock the full power of AI image processing
          </p>
        </div>

        {/* Pricing Plans */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-12">
          {pricingPlans.map((plan) => (
            <div
              key={plan.name}
              onClick={() => setSelectedPlan(plan.name.toLowerCase())}
              className={`relative bg-white dark:bg-gray-800 rounded-2xl shadow-xl p-8 cursor-pointer transition-all duration-200 ${
                selectedPlan === plan.name.toLowerCase()
                  ? "ring-4 ring-blue-500 transform scale-105"
                  : "hover:shadow-2xl"
              }`}
            >
              {plan.popular && (
                <div className="absolute top-0 right-0 bg-blue-600 text-white px-4 py-1 rounded-bl-xl rounded-tr-xl text-sm font-semibold">
                  Popular
                </div>
              )}
              <div className="text-center mb-6">
                <h3 className="text-2xl font-bold text-gray-900 dark:text-white mb-2">
                  {plan.name}
                </h3>
                <div className="flex items-baseline justify-center">
                  <span className="text-5xl font-extrabold text-gray-900 dark:text-white">
                    ${plan.price}
                  </span>
                  <span className="text-xl text-gray-500 dark:text-gray-400 ml-2">
                    /{plan.period}
                  </span>
                </div>
              </div>
              <ul className="space-y-4 mb-8">
                {plan.features.map((feature, index) => (
                  <li key={index} className="flex items-start">
                    <span className="text-green-500 mr-3 text-xl">✓</span>
                    <span className="text-gray-600 dark:text-gray-300">
                      {feature}
                    </span>
                  </li>
                ))}
              </ul>
              <div
                className={`text-center font-semibold py-2 px-4 rounded-lg ${
                  selectedPlan === plan.name.toLowerCase()
                    ? "bg-blue-600 text-white"
                    : "bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300"
                }`}
              >
                {selectedPlan === plan.name.toLowerCase()
                  ? "Selected"
                  : "Select Plan"}
              </div>
            </div>
          ))}
        </div>

        {/* Payment Form */}
        <div className="max-w-3xl mx-auto bg-white dark:bg-gray-800 rounded-2xl shadow-xl p-8">
          <h2 className="text-3xl font-bold text-gray-900 dark:text-white mb-8">
            Payment Details
          </h2>

          {/* Order Summary */}
          <div className="bg-blue-50 dark:bg-blue-900/20 rounded-xl p-6 mb-8">
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">
              Order Summary
            </h3>
            <div className="flex justify-between items-center mb-2">
              <span className="text-gray-600 dark:text-gray-300">
                {selectedPlanDetails?.name} Plan
              </span>
              <span className="text-gray-900 dark:text-white font-semibold">
                ${selectedPlanDetails?.price}/{selectedPlanDetails?.period}
              </span>
            </div>
            <div className="border-t border-gray-300 dark:border-gray-600 mt-4 pt-4">
              <div className="flex justify-between items-center">
                <span className="text-lg font-semibold text-gray-900 dark:text-white">
                  Total
                </span>
                <span className="text-2xl font-bold text-blue-600 dark:text-blue-400">
                  ${selectedPlanDetails?.price}
                </span>
              </div>
            </div>
          </div>

          {/* Payment Method Selection */}
          <div className="mb-8">
            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-4">
              Payment Method
            </label>
            <div className="grid grid-cols-2 gap-4">
              <button
                type="button"
                onClick={() => setPaymentMethod("card")}
                className={`p-4 border-2 rounded-lg font-medium transition-all ${
                  paymentMethod === "card"
                    ? "border-blue-500 bg-blue-50 dark:bg-blue-900/20 text-blue-700 dark:text-blue-300"
                    : "border-gray-300 dark:border-gray-600 text-gray-700 dark:text-gray-300 hover:border-blue-300"
                }`}
              >
                💳 Credit Card
              </button>
              <button
                type="button"
                onClick={() => setPaymentMethod("paypal")}
                className={`p-4 border-2 rounded-lg font-medium transition-all ${
                  paymentMethod === "paypal"
                    ? "border-blue-500 bg-blue-50 dark:bg-blue-900/20 text-blue-700 dark:text-blue-300"
                    : "border-gray-300 dark:border-gray-600 text-gray-700 dark:text-gray-300 hover:border-blue-300"
                }`}
              >
                🅿️ PayPal
              </button>
            </div>
          </div>

          <form onSubmit={handleSubmit} className="space-y-6">
            {/* Card Details (only for card payment) */}
            {paymentMethod === "card" && (
              <>
                <div>
                  <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                    Card Number
                  </label>
                  <input
                    type="text"
                    value={formData.cardNumber}
                    onChange={(e) =>
                      handleInputChange("cardNumber", formatCardNumber(e.target.value))
                    }
                    placeholder="1234 5678 9012 3456"
                    className={`w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent dark:bg-gray-700 dark:text-white ${
                      errors.cardNumber
                        ? "border-red-500"
                        : "border-gray-300 dark:border-gray-600"
                    }`}
                  />
                  {errors.cardNumber && (
                    <p className="text-red-500 text-sm mt-1">{errors.cardNumber}</p>
                  )}
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                    Cardholder Name
                  </label>
                  <input
                    type="text"
                    value={formData.cardName}
                    onChange={(e) => handleInputChange("cardName", e.target.value)}
                    placeholder="John Doe"
                    className={`w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent dark:bg-gray-700 dark:text-white ${
                      errors.cardName
                        ? "border-red-500"
                        : "border-gray-300 dark:border-gray-600"
                    }`}
                  />
                  {errors.cardName && (
                    <p className="text-red-500 text-sm mt-1">{errors.cardName}</p>
                  )}
                </div>

                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                      Expiry Date
                    </label>
                    <input
                      type="text"
                      value={formData.expiryDate}
                      onChange={(e) =>
                        handleInputChange("expiryDate", formatExpiryDate(e.target.value))
                      }
                      placeholder="MM/YY"
                      maxLength={5}
                      className={`w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent dark:bg-gray-700 dark:text-white ${
                        errors.expiryDate
                          ? "border-red-500"
                          : "border-gray-300 dark:border-gray-600"
                      }`}
                    />
                    {errors.expiryDate && (
                      <p className="text-red-500 text-sm mt-1">{errors.expiryDate}</p>
                    )}
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                      CVV
                    </label>
                    <input
                      type="text"
                      value={formData.cvv}
                      onChange={(e) =>
                        handleInputChange("cvv", e.target.value.replace(/\D/g, "").slice(0, 3))
                      }
                      placeholder="123"
                      maxLength={3}
                      className={`w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent dark:bg-gray-700 dark:text-white ${
                        errors.cvv
                          ? "border-red-500"
                          : "border-gray-300 dark:border-gray-600"
                      }`}
                    />
                    {errors.cvv && (
                      <p className="text-red-500 text-sm mt-1">{errors.cvv}</p>
                    )}
                  </div>
                </div>
              </>
            )}

            {/* PayPal Message */}
            {paymentMethod === "paypal" && (
              <div className="bg-yellow-50 dark:bg-yellow-900/20 border border-yellow-200 dark:border-yellow-800 rounded-lg p-4">
                <p className="text-yellow-800 dark:text-yellow-300">
                  You will be redirected to PayPal to complete your payment securely.
                </p>
              </div>
            )}

            {/* Billing Information */}
            <div className="border-t border-gray-200 dark:border-gray-700 pt-6">
              <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">
                Billing Information
              </h3>

              <div className="space-y-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                    Email Address
                  </label>
                  <input
                    type="email"
                    value={formData.email}
                    onChange={(e) => handleInputChange("email", e.target.value)}
                    placeholder="john@example.com"
                    className={`w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent dark:bg-gray-700 dark:text-white ${
                      errors.email
                        ? "border-red-500"
                        : "border-gray-300 dark:border-gray-600"
                    }`}
                  />
                  {errors.email && (
                    <p className="text-red-500 text-sm mt-1">{errors.email}</p>
                  )}
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                    Billing Address
                  </label>
                  <input
                    type="text"
                    value={formData.billingAddress}
                    onChange={(e) => handleInputChange("billingAddress", e.target.value)}
                    placeholder="123 Main Street"
                    className={`w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent dark:bg-gray-700 dark:text-white ${
                      errors.billingAddress
                        ? "border-red-500"
                        : "border-gray-300 dark:border-gray-600"
                    }`}
                  />
                  {errors.billingAddress && (
                    <p className="text-red-500 text-sm mt-1">{errors.billingAddress}</p>
                  )}
                </div>

                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                      City
                    </label>
                    <input
                      type="text"
                      value={formData.city}
                      onChange={(e) => handleInputChange("city", e.target.value)}
                      placeholder="New York"
                      className={`w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent dark:bg-gray-700 dark:text-white ${
                        errors.city
                          ? "border-red-500"
                          : "border-gray-300 dark:border-gray-600"
                      }`}
                    />
                    {errors.city && (
                      <p className="text-red-500 text-sm mt-1">{errors.city}</p>
                    )}
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                      ZIP Code
                    </label>
                    <input
                      type="text"
                      value={formData.zipCode}
                      onChange={(e) => handleInputChange("zipCode", e.target.value)}
                      placeholder="10001"
                      className={`w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent dark:bg-gray-700 dark:text-white ${
                        errors.zipCode
                          ? "border-red-500"
                          : "border-gray-300 dark:border-gray-600"
                      }`}
                    />
                    {errors.zipCode && (
                      <p className="text-red-500 text-sm mt-1">{errors.zipCode}</p>
                    )}
                  </div>
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                    Country
                  </label>
                  <input
                    type="text"
                    value={formData.country}
                    onChange={(e) => handleInputChange("country", e.target.value)}
                    placeholder="United States"
                    className={`w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent dark:bg-gray-700 dark:text-white ${
                      errors.country
                        ? "border-red-500"
                        : "border-gray-300 dark:border-gray-600"
                    }`}
                  />
                  {errors.country && (
                    <p className="text-red-500 text-sm mt-1">{errors.country}</p>
                  )}
                </div>
              </div>
            </div>

            {/* Submit Button */}
            <button
              type="submit"
              disabled={isProcessing}
              className="w-full bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400 text-white font-bold py-4 px-6 rounded-lg transition-colors duration-200 disabled:cursor-not-allowed text-lg"
            >
              {isProcessing
                ? "Processing..."
                : `Pay $${selectedPlanDetails?.price} - Complete Purchase`}
            </button>

            <p className="text-center text-sm text-gray-500 dark:text-gray-400 mt-4">
              🔒 Your payment information is secure and encrypted
            </p>
          </form>
        </div>
      </div>
    </div>
  );
}
