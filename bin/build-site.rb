require 'yaml'
require 'tempfile'
configs = ARGV.empty? ? ['_config.yml'] : ARGV
settings = configs.reduce({}) { |result, path| result.merge(YAML.load_file(path)) }
root_base = settings.fetch('baseurl', '').to_s.sub(%r{/$}, '')
destination = settings.fetch('destination', '_site')
[['zh-CN', root_base, destination], ['en', "#{root_base}/en", "#{destination}/en"]].each do |lang, base, output|
  Tempfile.create(['alchemist-language', '.yml']) do |file|
    config = {'lang' => lang, 'baseurl' => base, 'language_root' => root_base, 'destination' => output}
    config['description'] = 'Alchemist — a personal notebook on research, reading, and reflection.' if lang == 'en'
    file.write(config.to_yaml)
    file.flush
    success = system('bundle', 'exec', 'jekyll', 'build', '--config', (configs + [file.path]).join(','), '--trace')
    abort "Build failed: #{lang}" unless success
  end
end
