CREATE PROCEDURE countriesSelection()
BEGIN
	select * from countries where continent='Africa';
END
