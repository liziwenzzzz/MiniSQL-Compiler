tokens = (
    # Reserverd words
    # A
    'ADD','ALL', 'ALTER','ANALYZE','AND','AS','ASC','ASENSITIVE', 'AUTOCOMMIT', 'OFF', 'WHENEVER','SQLERROR', 'ROLLBACK', 'AUTHORIZATION',
    'ANY',

    # B
    'BEFORE','BETWEEN','BIGINT','BINARY','BLOB','BOTH', 'BY',

    # C
    'CALL','CASCADE','CASE','CHANGE','CHAR','CHARACTER','CHECK','COLLATE','COLUMN','CONDITION','CONSTRAINT',
    'CONTINUE','CONVERT','CREATE','CROSS','CURRENT_DATE','CURRENT_TIME','CURRENT_TIMESTAMP','CURRENT_USER','CURSOR', 'CLOSE', 'CURRENT', 'COMPARISON',
    'COMMIT',
    
    # D
    'DATABASE','DATABASES','DAY_HOUR','DAY_MICROSECOND','DAY_MINUTE','DAY_SECOND','DEC','DECIMAL','DECLARE','DEFAULT','DELAYED',
    'DELETE','DESC','DESCRIBE','DETERMINISTIC','DISTINCT','DISTINCTROW','DIV','DOUBLE','DROP','DUAL', 'DATE',

    # E
    'EACH','ELSE','ELSEIF','ENCLOSED','ESCAPED','EXISTS','EXIT','EXPLAIN','ESCAPE',

    # F
    'FALSE','FETCH','FLOAT','FLOAT4','FLOAT8','FOR','FORCE','FOREIGN','FROM','FULLTEXT',

    # G
    'GRANT','GROUP',

    # H
    'HAVING','HIGH_PRIORITY','HOUR_MICROSECOND','HOUR_MINUTE','HOUR_SECOND',

    # I
    'IF','IGNORE','IN','INDEX','INFILE','INNER','INOUT','INSENSITIVE','INSERT','INT','INT1',
    'INT2','INT3','INT4','INT8','INTEGER','INTERVAL','INTO','IS','ITERATE', 'INDICATOR',

    # J
    'JOIN',

    # K
    'KEY','KEYS','KILL',

    # L
    'LEADING','LEAVE','LEFT','LIKE','LIMIT','LINES','LOAD','LOCALTIME','LOCALTIMESTAMP',
    'LOCK','LONG','LONGBLOB','LONGTEXT','LOOP','LOW_PRIORITY',

    # M
    'MATCH','MEDIUMBLOB','MEDIUMINT','MEDIUMTEXT','MIDDLEINT','MINUTE_MICROSECOND',
    'MINUTE_SECOND','MOD','MODIFIES',

    # N
    'NATURAL','NOT','NO_WRITE_TO_BINLOG','NULL','NUMERIC', 'NL',

    # O
    'ON','OPTIMIZE','OPTION','OPTIONALLY','OR','ORDER','OUT','OUTER','OUTFILE', 'OF','OPEN',

    # P
    'PRECISION','PRIMARY','PROCEDURE','PURGE', 'PRIVILEGES', 'PUBLIC',

    # R
    'READ','READS','REAL','REFERENCES','REGEXP','RELEASE','RENAME','REPEAT','REPLACE','REQUIRE',
    'RESTRICT','RETURN','REVOKE','RIGHT','RLIKE',

    # S
    'SCHEMA','SCHEMAS','SECOND_MICROSECOND','SELECT','SENSITIVE','SEPARATOR','SET','SHOW','SMALLINT','SONAME',
    'SPATIAL','SPECIFIC','SQL','SQLEXCEPTION','SQLSTATE','SQLWARNING','SQL_BIG_RESULT','SQL_CALC_FOUND_ROWS','SQL_SMALL_RESULT',
    'SSL','STARTING','STRAIGHT_JOIN', 'SOME',

    # T
    'TABLE','TERMINATED','THEN','TINYBLOB','TINYINT','TINYTEXT','TO','TRAILING','TRIGGER','TRUE',

    # U
    'UNDO','UNION','UNIQUE','UNLOCK','UNSIGNED','UPDATE','USAGE','USE','USING','UTC_DATE','UTC_TIME','UTC_TIMESTAMP', 'USER',

    # V
    'VALUES', 'VARBINARY','VARCHAR', 'VARCHARACTER', 'VARYING', 'VIEW',

    # W
    'WHEN','WHERE','WHILE','WITH', 'WRITE', 'WORK',

    # X
    'XOR',

    # Y
    'YEAR_MONTH',

    # Z
    'ZEROFILL',
     
    # Symbols
    'PLUS',
    'PLUSPLUS',
    #'PLUSEQUAL',
    'MINUS',
    'MINUSMINUS',
    #'MINUSEQUAL',
    'TIMES',
    'DIVIDE',
    'LESS',
    'LESSEQUAL',
    'GREATER',
    'GREATEREQUAL',
    'EQUAL',
    'DEQUAL',
    'DISTINT',
    'ISEQUAL',
    'SEMICOLON',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBLOCK',
    'RBLOCK',
    'COLON',
    'AMPERSANT',
    'HASHTAG',
    'DOT',

    # Others   
    'ID', 
    'NUMBER',
)