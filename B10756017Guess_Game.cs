using System;

namespace Guess_game
{
    class Program
    {
        static void Main(string[] args)
        {
            string ans;
            do
            {
                Console.WriteLine("Guess Game:\r\nQuestion:NBA2019-2020賽季中因何事延後賽程？\r\n1.SARS 2.H1N1 3.HIV 4.AIDS 5.天花 6.霍亂 7.鼠疫 8.COVID-19 9.瘧疾 10.結核病");
                ans = Console.ReadLine();
                int a = int.Parse(ans);
                if (a >= 1 && a <= 10)
                {
                    if (ans != "8")
                        Console.WriteLine("wrong answer\r\n");
                    else
                        Console.WriteLine("right answer");
                }
                else
                    Console.WriteLine("輸入錯誤請重新輸入\r\n");
            }while(ans != "8");
            Console.ReadLine();
        }
    }
}
