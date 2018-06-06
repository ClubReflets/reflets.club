from flask_assets import Bundle

css = Bundle(
  'scss/main.scss',
  filters=['pyscss', 'cssmin'],
  output='out/style.css')

js = Bundle(
  'js/app.js',
  filters='jsmin',
  output='out/app.js')