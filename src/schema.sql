CREATE TABLE Books (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  key TEXT NOT NULL,
  title TEXT NOT NULL,
  year TEXT NOT NULL,
  author TEXT NOT NULL,
  publisher TEXT NOT NULL,
  address TEXT
  )

CREATE TABLE Articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  key TEXT NOT NULL,
  title TEXT NOT NULL,
  year TEXT NOT NULL,
  author TEXT NOT NULL,
  journal TEXT NOT NULL,
  pages TEXT,
  volume TEXT,
  month TEXT,
  doi TEXT
  )