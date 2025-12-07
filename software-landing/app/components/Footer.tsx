export default function Footer() {
  return (
    <footer className="bg-gray-900 text-gray-300">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div className="col-span-1 md:col-span-2">
            <span className="text-2xl font-bold bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">
              Innovate
            </span>
            <p className="mt-4 text-gray-400 max-w-md">
              Building tomorrow's solutions today. We deliver cutting-edge software solutions that transform businesses and drive innovation.
            </p>
          </div>

          <div>
            <h3 className="text-white font-semibold mb-4">Company</h3>
            <ul className="space-y-2">
              <li>
                <a href="#about" className="hover:text-blue-400 transition-colors">About Us</a>
              </li>
              <li>
                <a href="#services" className="hover:text-blue-400 transition-colors">Services</a>
              </li>
              <li>
                <a href="#careers" className="hover:text-blue-400 transition-colors">Careers</a>
              </li>
              <li>
                <a href="#contact" className="hover:text-blue-400 transition-colors">Contact</a>
              </li>
            </ul>
          </div>

          <div>
            <h3 className="text-white font-semibold mb-4">Resources</h3>
            <ul className="space-y-2">
              <li>
                <a href="#blog" className="hover:text-blue-400 transition-colors">Blog</a>
              </li>
              <li>
                <a href="#docs" className="hover:text-blue-400 transition-colors">Documentation</a>
              </li>
              <li>
                <a href="#support" className="hover:text-blue-400 transition-colors">Support</a>
              </li>
              <li>
                <a href="#privacy" className="hover:text-blue-400 transition-colors">Privacy Policy</a>
              </li>
            </ul>
          </div>
        </div>

        <div className="mt-12 pt-8 border-t border-gray-800 flex flex-col md:flex-row justify-between items-center">
          <p className="text-gray-400 text-sm">
            © 2025 Innovate Software. All rights reserved.
          </p>
          <div className="flex space-x-6 mt-4 md:mt-0">
            <a href="#" className="text-gray-400 hover:text-blue-400 transition-colors">
              Twitter
            </a>
            <a href="#" className="text-gray-400 hover:text-blue-400 transition-colors">
              LinkedIn
            </a>
            <a href="#" className="text-gray-400 hover:text-blue-400 transition-colors">
              GitHub
            </a>
          </div>
        </div>
      </div>
    </footer>
  );
}
