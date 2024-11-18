using System;

namespace calculadoraBasica_1
{
    public class Calculadora
    {
        public static double Operar(double num1,double num2, string OP )
        {
            switch (OP)
            {
                case "+":
                    return num1 + num2;
                case "-":
                    return num1 - num2;
                case "*":  
                    return num1 * num2;
                case "/":
                    if (num2 == 0)
                    {
                        throw new DivideByZeroException("Error: No se puede dividir entre cero.");
                    }
                    return num1 / num2;
                default:
                    throw new ArgumentException("Error: Operador no valido.");
            }
        }
    }
}
