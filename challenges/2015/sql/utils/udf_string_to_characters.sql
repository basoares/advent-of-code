CREATE FUNCTION [dbo].[udf_string_to_characters]
(
   @string NVARCHAR(MAX)
)
RETURNS TABLE WITH SCHEMABINDING AS
RETURN
  SELECT SUBSTRING(@string, N.N, 1) AS C, N.N
    FROM dbo.tbl_numbers N
   WHERE N <= LEN(@string)
;
