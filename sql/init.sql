-- Docs https://github.com/cipherstash/encrypt-query-language/?tab=readme-ov-file#getting-started
-- These commands have already been executed and part of the database initialization

CREATE TABLE IF NOT EXISTS pycon_cta (
  id SERIAL PRIMARY KEY,
  key "cs_encrypted_v1"
);

SELECT cs_add_index_v1(
  'pycon_cta',
  'key',
  'match',
  'text',
  '{"token_filters": [{"kind": "downcase"}], "tokenizer": { "kind": "ngram", "token_length": 3 }}'
);

SELECT cs_encrypt_v1();
SELECT cs_activate_v1();