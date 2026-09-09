require "yaml"
require "uri"
repo = ENV.fetch("GITHUB_REPOSITORY")
abort "Expected owner/repository" unless repo.match?(%r{\A[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+\z})
owner, name = repo.split("/")
url = ENV.fetch("SITE_URL", "").strip
url = "https://#{owner.downcase}.github.io" if url.empty?
uri = URI.parse(url)
abort "SITE_URL must be an HTTPS origin" unless uri.scheme == "https" && uri.host && ["", "/"].include?(uri.path) && !uri.query && !uri.fragment
base = ENV["SITE_BASEURL"]
base = name.downcase == "#{owner.downcase}.github.io" ? "" : "/#{name}" if base.nil? || base.empty?
base = "" if base == "/"
abort "Invalid SITE_BASEURL" unless base.empty? || base.match?(%r{\A/[A-Za-z0-9_/-]+\z})
File.write("_config.deploy.yml", {"url" => url.sub(%r{/$}, ""), "baseurl" => base}.to_yaml)
