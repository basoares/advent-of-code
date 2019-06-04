/*

Advent of Code - 2015
--- Day 1: Repose Record --

Released under the MIT License <http://opensource.org/licenses/mit-license.php>

*/

;WITH INPUT_D01 AS 
(
    SELECT REPLACE(F.C, CHAR(10), '') AS RECORD
      FROM OPENROWSET(BULK 'advent-of-code\challenges\2015\input\d01.txt', SINGLE_CLOB) INPUT_FILE(FILE_DATA)
     CROSS APPLY Staging.dbo.udf_string_to_characters(INPUT_FILE.FILE_DATA) F
)
SELECT SUM(CASE WHEN RECORD = '(' THEN 1 ELSE -1 END) AS PART_1
  FROM INPUT_D01


;WITH INPUT_D01 AS 
(
    SELECT REPLACE(F.C, CHAR(10), '') AS RECORD, F.N
      FROM OPENROWSET(BULK 'advent-of-code\challenges\2015\input\d01.txt', SINGLE_CLOB) INPUT_FILE(FILE_DATA)
     CROSS APPLY Staging.dbo.udf_string_to_characters(INPUT_FILE.FILE_DATA) F
), RUNNING_FLOORS AS
(
	SELECT SUM(CASE WHEN RECORD = '(' THEN 1 ELSE -1 END) OVER (ORDER BY N) AS F, N
      FROM INPUT_D01
)
SELECT MIN(N)
  FROM RUNNING_FLOORS
 WHERE F = -1