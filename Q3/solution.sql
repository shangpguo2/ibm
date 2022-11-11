SELECT owner.owner_id, owner.owner_name, COUNT(category_article_mapping.category_id) AS different_category_count
FROM owner
INNER JOIN article ON article.owner_id = owner.owner_id
INNER JOIN category_article_mapping ON article.article_id = category_article_mapping.article_id
GROUP BY owner.owner_id
ORDER BY COUNT(category_article_mapping.category_id) DESC;