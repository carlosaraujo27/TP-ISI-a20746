CREATE DATABASE EventosCalendarDB;
GO

USE EventosCalendarDB;
GO

-- Criar a tabela
CREATE TABLE Eventos (
    ID INT IDENTITY(1,1) PRIMARY KEY,
    Evento_Title NVARCHAR(255),        -- T�tulo do evento
    Start_Date DATETIME,               -- Data e hora de in�cio
    End_Date DATETIME,                 -- Data e hora de fim
    Location NVARCHAR(255),            -- Localiza��o do evento
    Status NVARCHAR(50)                -- Status do evento
);
GO

--Testar
--SELECT * FROM Eventos;
