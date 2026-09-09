# Apply authored translations before pagination, feed, search and metadata generation.
Jekyll::Hooks.register :site, :post_read do |site|
  next unless site.config['lang'] == 'en'
  documents = site.pages + site.collections.values.flat_map(&:docs)
  documents.each do |document|
    translation = document.data.fetch('translations', {})['en']
    if document.is_a?(Jekyll::Document) && document.collection.label == 'posts' && !translation
      raise Jekyll::Errors::FatalException, "Missing English translation: #{document.relative_path}"
    end
    next unless translation
    if document.is_a?(Jekyll::Document) && document.collection.label == 'posts'
      %w[title description body].each do |field|
        raise Jekyll::Errors::FatalException, "Missing English #{field}: #{document.relative_path}" if translation[field].to_s.strip.empty?
      end
    end
    translation.each { |key, value| document.data[key] = value unless key == 'body' }
    document.content = translation['body'] if translation['body']
  end
end
