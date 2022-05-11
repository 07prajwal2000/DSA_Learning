namespace CsharpProject
{
    public class EncodeCharacters
    {
        public static string key = "RLTDRRTRS2S1";
        public static string value = "123456";

        public static string EncodeCharacter(string key, string value)
        {
            Span<char> val = new(value.ToArray());
            var index = 0;
            for (var i = 0; i < key.Length; i++)
            {
                switch (key[i])
                {
                    case 'R':
                        index ++;
                        break;
                        
                    case 'L':
                        index --;
                        break;
                        
                    case 'T':
                        val[index]++;
                        break;
                        
                    case 'D':
                        val[index]--;
                        break;

                    case 'S':
                        i++;
                        var swapPos = int.Parse(key[i].ToString()) - 1;
                        var temp = val[index];
                        val[index] = val[swapPos];
                        val[swapPos] = temp;
                        break;
                }
            }
            return val.ToString();
        }

    }
}