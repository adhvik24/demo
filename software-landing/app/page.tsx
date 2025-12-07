import Navigation from "./components/Navigation";
import Footer from "./components/Footer";

export default function Home() {
  return (
    <div className="min-h-screen">
      <Navigation />

      {/* Hero Section */}
      <section className="pt-32 pb-20 px-4 sm:px-6 lg:px-8 bg-gradient-to-br from-blue-50 via-purple-50 to-pink-50 dark:from-gray-900 dark:via-blue-900/20 dark:to-purple-900/20">
        <div className="max-w-7xl mx-auto text-center">
          <h1 className="text-5xl md:text-7xl font-bold mb-6 bg-gradient-to-r from-blue-600 via-purple-600 to-pink-600 bg-clip-text text-transparent">
            Building Tomorrow's
            <br />
            Solutions Today
          </h1>
          <p className="text-xl md:text-2xl text-gray-600 dark:text-gray-300 mb-8 max-w-3xl mx-auto">
            Transform your business with cutting-edge software solutions. We deliver innovation, reliability, and excellence.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <button className="px-8 py-4 bg-gradient-to-r from-blue-600 to-purple-600 text-white rounded-lg text-lg font-semibold hover:shadow-2xl hover:scale-105 transition-all duration-200">
              Start Your Project
            </button>
            <button className="px-8 py-4 bg-white dark:bg-gray-800 text-gray-900 dark:text-white rounded-lg text-lg font-semibold border-2 border-gray-300 dark:border-gray-700 hover:border-blue-600 dark:hover:border-blue-400 hover:shadow-lg transition-all duration-200">
              View Our Work
            </button>
          </div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="py-16 bg-white dark:bg-gray-900">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
            <div>
              <div className="text-4xl md:text-5xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent mb-2">
                500+
              </div>
              <div className="text-gray-600 dark:text-gray-400">Projects Delivered</div>
            </div>
            <div>
              <div className="text-4xl md:text-5xl font-bold bg-gradient-to-r from-purple-600 to-pink-600 bg-clip-text text-transparent mb-2">
                200+
              </div>
              <div className="text-gray-600 dark:text-gray-400">Happy Clients</div>
            </div>
            <div>
              <div className="text-4xl md:text-5xl font-bold bg-gradient-to-r from-pink-600 to-red-600 bg-clip-text text-transparent mb-2">
                50+
              </div>
              <div className="text-gray-600 dark:text-gray-400">Team Members</div>
            </div>
            <div>
              <div className="text-4xl md:text-5xl font-bold bg-gradient-to-r from-blue-600 to-cyan-600 bg-clip-text text-transparent mb-2">
                10+
              </div>
              <div className="text-gray-600 dark:text-gray-400">Years Experience</div>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="py-20 px-4 sm:px-6 lg:px-8 bg-gray-50 dark:bg-gray-800">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-4xl md:text-5xl font-bold mb-4 text-gray-900 dark:text-white">
              Why Choose Us
            </h2>
            <p className="text-xl text-gray-600 dark:text-gray-300 max-w-2xl mx-auto">
              We combine expertise, innovation, and dedication to deliver exceptional results
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="bg-white dark:bg-gray-900 p-8 rounded-2xl shadow-lg hover:shadow-2xl transition-shadow duration-300">
              <div className="w-12 h-12 bg-gradient-to-r from-blue-600 to-purple-600 rounded-lg mb-6"></div>
              <h3 className="text-2xl font-bold mb-4 text-gray-900 dark:text-white">
                Innovative Solutions
              </h3>
              <p className="text-gray-600 dark:text-gray-300">
                Cutting-edge technology and creative approaches to solve complex business challenges
              </p>
            </div>

            <div className="bg-white dark:bg-gray-900 p-8 rounded-2xl shadow-lg hover:shadow-2xl transition-shadow duration-300">
              <div className="w-12 h-12 bg-gradient-to-r from-purple-600 to-pink-600 rounded-lg mb-6"></div>
              <h3 className="text-2xl font-bold mb-4 text-gray-900 dark:text-white">
                Expert Team
              </h3>
              <p className="text-gray-600 dark:text-gray-300">
                Skilled professionals with years of experience in software development and design
              </p>
            </div>

            <div className="bg-white dark:bg-gray-900 p-8 rounded-2xl shadow-lg hover:shadow-2xl transition-shadow duration-300">
              <div className="w-12 h-12 bg-gradient-to-r from-pink-600 to-red-600 rounded-lg mb-6"></div>
              <h3 className="text-2xl font-bold mb-4 text-gray-900 dark:text-white">
                24/7 Support
              </h3>
              <p className="text-gray-600 dark:text-gray-300">
                Round-the-clock assistance to ensure your systems run smoothly at all times
              </p>
            </div>

            <div className="bg-white dark:bg-gray-900 p-8 rounded-2xl shadow-lg hover:shadow-2xl transition-shadow duration-300">
              <div className="w-12 h-12 bg-gradient-to-r from-cyan-600 to-blue-600 rounded-lg mb-6"></div>
              <h3 className="text-2xl font-bold mb-4 text-gray-900 dark:text-white">
                Scalable Architecture
              </h3>
              <p className="text-gray-600 dark:text-gray-300">
                Build solutions that grow with your business, from startup to enterprise
              </p>
            </div>

            <div className="bg-white dark:bg-gray-900 p-8 rounded-2xl shadow-lg hover:shadow-2xl transition-shadow duration-300">
              <div className="w-12 h-12 bg-gradient-to-r from-green-600 to-emerald-600 rounded-lg mb-6"></div>
              <h3 className="text-2xl font-bold mb-4 text-gray-900 dark:text-white">
                Agile Development
              </h3>
              <p className="text-gray-600 dark:text-gray-300">
                Fast iterations and continuous delivery to bring your product to market quickly
              </p>
            </div>

            <div className="bg-white dark:bg-gray-900 p-8 rounded-2xl shadow-lg hover:shadow-2xl transition-shadow duration-300">
              <div className="w-12 h-12 bg-gradient-to-r from-orange-600 to-yellow-600 rounded-lg mb-6"></div>
              <h3 className="text-2xl font-bold mb-4 text-gray-900 dark:text-white">
                Security First
              </h3>
              <p className="text-gray-600 dark:text-gray-300">
                Enterprise-grade security measures to protect your data and users
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Services Section */}
      <section id="services" className="py-20 px-4 sm:px-6 lg:px-8 bg-white dark:bg-gray-900">
        <div className="max-w-7xl mx-auto">
          <div className="text-center mb-16">
            <h2 className="text-4xl md:text-5xl font-bold mb-4 text-gray-900 dark:text-white">
              Our Services
            </h2>
            <p className="text-xl text-gray-600 dark:text-gray-300 max-w-2xl mx-auto">
              Comprehensive software solutions tailored to your business needs
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div className="group p-8 rounded-2xl bg-gradient-to-br from-blue-50 to-purple-50 dark:from-blue-900/20 dark:to-purple-900/20 hover:shadow-2xl transition-all duration-300">
              <h3 className="text-2xl font-bold mb-4 text-gray-900 dark:text-white">
                Web Development
              </h3>
              <p className="text-gray-600 dark:text-gray-300 mb-4">
                Custom web applications built with modern frameworks and best practices. Responsive, fast, and user-friendly.
              </p>
              <ul className="space-y-2 text-gray-600 dark:text-gray-300">
                <li className="flex items-start">
                  <span className="mr-2">•</span>
                  <span>React, Next.js, Vue.js</span>
                </li>
                <li className="flex items-start">
                  <span className="mr-2">•</span>
                  <span>Progressive Web Apps</span>
                </li>
                <li className="flex items-start">
                  <span className="mr-2">•</span>
                  <span>E-commerce Solutions</span>
                </li>
              </ul>
            </div>

            <div className="group p-8 rounded-2xl bg-gradient-to-br from-purple-50 to-pink-50 dark:from-purple-900/20 dark:to-pink-900/20 hover:shadow-2xl transition-all duration-300">
              <h3 className="text-2xl font-bold mb-4 text-gray-900 dark:text-white">
                Mobile Development
              </h3>
              <p className="text-gray-600 dark:text-gray-300 mb-4">
                Native and cross-platform mobile apps that deliver exceptional user experiences on iOS and Android.
              </p>
              <ul className="space-y-2 text-gray-600 dark:text-gray-300">
                <li className="flex items-start">
                  <span className="mr-2">•</span>
                  <span>React Native, Flutter</span>
                </li>
                <li className="flex items-start">
                  <span className="mr-2">•</span>
                  <span>iOS & Android Native</span>
                </li>
                <li className="flex items-start">
                  <span className="mr-2">•</span>
                  <span>App Store Optimization</span>
                </li>
              </ul>
            </div>

            <div className="group p-8 rounded-2xl bg-gradient-to-br from-pink-50 to-red-50 dark:from-pink-900/20 dark:to-red-900/20 hover:shadow-2xl transition-all duration-300">
              <h3 className="text-2xl font-bold mb-4 text-gray-900 dark:text-white">
                Cloud Solutions
              </h3>
              <p className="text-gray-600 dark:text-gray-300 mb-4">
                Scalable cloud infrastructure and migration services to power your digital transformation.
              </p>
              <ul className="space-y-2 text-gray-600 dark:text-gray-300">
                <li className="flex items-start">
                  <span className="mr-2">•</span>
                  <span>AWS, Azure, Google Cloud</span>
                </li>
                <li className="flex items-start">
                  <span className="mr-2">•</span>
                  <span>DevOps & CI/CD</span>
                </li>
                <li className="flex items-start">
                  <span className="mr-2">•</span>
                  <span>Cloud Migration</span>
                </li>
              </ul>
            </div>

            <div className="group p-8 rounded-2xl bg-gradient-to-br from-cyan-50 to-blue-50 dark:from-cyan-900/20 dark:to-blue-900/20 hover:shadow-2xl transition-all duration-300">
              <h3 className="text-2xl font-bold mb-4 text-gray-900 dark:text-white">
                AI & Machine Learning
              </h3>
              <p className="text-gray-600 dark:text-gray-300 mb-4">
                Intelligent solutions powered by artificial intelligence and machine learning technologies.
              </p>
              <ul className="space-y-2 text-gray-600 dark:text-gray-300">
                <li className="flex items-start">
                  <span className="mr-2">•</span>
                  <span>Predictive Analytics</span>
                </li>
                <li className="flex items-start">
                  <span className="mr-2">•</span>
                  <span>Natural Language Processing</span>
                </li>
                <li className="flex items-start">
                  <span className="mr-2">•</span>
                  <span>Computer Vision</span>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section id="contact" className="py-20 px-4 sm:px-6 lg:px-8 bg-gradient-to-r from-blue-600 via-purple-600 to-pink-600">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-4xl md:text-5xl font-bold mb-6 text-white">
            Ready to Start Your Project?
          </h2>
          <p className="text-xl text-white/90 mb-8">
            Let's discuss how we can help transform your ideas into reality
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <button className="px-8 py-4 bg-white text-purple-600 rounded-lg text-lg font-semibold hover:shadow-2xl hover:scale-105 transition-all duration-200">
              Schedule a Consultation
            </button>
            <button className="px-8 py-4 bg-transparent text-white rounded-lg text-lg font-semibold border-2 border-white hover:bg-white hover:text-purple-600 transition-all duration-200">
              View Case Studies
            </button>
          </div>
        </div>
      </section>

      <Footer />
    </div>
  );
}
