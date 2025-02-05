/*
create_at: 2025-02-50 10:05
update_at: 2025-02-50 13:55

@author: ronald.barberi

Read Me: 
*/

// Imported libraries

import java.time.LocalDate
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter
import java.time.format.DateTimeParseException

//  Create class
class ValidatorAllParameters {

    List<String> errors = []

    def funValidatorToNumItemsInt(int_item, int minimum_value, boolean value_empty = false) {

        if(value_empty) {
            int_item = (int_item == null || int_item.trim() == "") ? "0" : int_item
        }

        if(!value_empty && (int_item.trim() == "" || int_item == null || !int_item)) {
            errors << "Value is empty."
        } else {
            if(int_item.toInteger() <= minimum_value) {
                errors << "Value is less than: " + int_item
            }
        }
    }


    def funValidatorToNumItemsString(def str_item, def min_lengths, boolean various_strings, boolean various_lengths, boolean value_empty = false) {
        
        if (various_strings && str_item instanceof String) {
            str_item = [str_item]
        }
        if (!(str_item instanceof List)) {
            str_item = [str_item]
        }

        if (various_lengths && min_lengths instanceof String) {
            min_lengths = [min_lengths]
        }
        if (!(min_lengths instanceof List)) {
            min_lengths = [min_lengths]
        }

        str_item.each { t ->
            if (t == null || (t instanceof String && t.trim().isEmpty())) {
                if (value_empty) {
                    t = "0"
                } else {
                    errors << "Value is empty."
                    return
                }
            }
            
            if (!(t.length() in min_lengths*.toInteger())) {
                errors << "The item '${t}' does not have the required length."
            }
        }
    }


    def funValidatorDates(String date_start_in, String date_end_in, boolean isDatetime = false) {

        def format_date = DateTimeFormatter.ofPattern("yyyy-MM-dd")
        def format_datetime = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")

        if ((date_start_in == null || date_start_in.trim() == "" || !date_start_in) || (date_end_in == null || date_end_in.trim() == "" || !date_end_in)) {
            errors << "Dates cannot be empty."
            return
        }

        
        if(isDatetime) {
            LocalDate date_formated_start = null
            LocalDate date_formated_end = null

            try {
                date_formated_start = LocalDateTime.parse(date_start_in, format_datetime)
                date_formated_end = LocalDateTime.parse(date_end_in, format_datetime)
                if (date_formated_start.isAfter(date_formated_end)) {
                    errors << "The date_start_in is less than the date_end_in"
                }
            } catch (DateTimeParseException e) {
                errors << "Invalid date value: ${e.getParsedString()}"
            }
        } else {
            LocalDate date_formated_start = null
            LocalDate date_formated_end = null

            try {
                date_formated_start = LocalDate.parse(date_start_in, format_date)
                date_formated_end = LocalDate.parse(date_end_in, format_date)
                if (date_formated_start.isAfter(date_formated_end)) {
                    errors << "The date_start_in is less than the date_end_in"
                }
            } catch (DateTimeParseException e) {
                errors << "Invalid values the field"
            }
        }
    }


    def funObtenerErrores() {
        return errors.isEmpty() ? null : errors.join("; ")
    }

}

// Use class

def filasPorPagina = ""
def fechaInicio = "2025-01-29"
def fechaFin = "2025-01-30"
def tarjeta = ["1234"]
def largo = [4, 6]

def validator = new ValidatorAllParameters()
validator.funValidatorToNumItemsInt(filasPorPagina, 0, false)
validator.funValidatorToNumItemsString(tarjeta, largo, false, true)
validator.funValidatorDates(fechaInicio, fechaFin, false)
def errores = validator.funObtenerErrores()
println(errores)
