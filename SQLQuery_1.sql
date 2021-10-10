-- Create a new table called '[gl_daily_rates]' in schema '[dbo]'
-- Drop the table if it already exists
IF OBJECT_ID('[dbo].[gl_daily_rates]', 'U') IS NOT NULL
DROP TABLE [dbo].[gl_daily_rates]
GO
-- Create the table in the specified schema
CREATE TABLE [dbo].[gl_daily_rates]
(
    [FROM_CURRENCY] NVARCHAR(15) NOT NULL, -- Primary Key column
    [TO_CURRENCY] NVARCHAR(15) NOT NULL,
    [FROM_CONVERSION_DATE] DATE NOT NULL,
    [TO_CONVERSION_DATE] DATE NOT NULL,
    [USER_CONVERSION_TYPE] NVARCHAR(50) NOT NULL,
    [CONVERSION_RATE] float NOT NULL,
    [MODE_FLAG] NVARCHAR(15) NOT NULL
    -- Specify more columns here
);
GO