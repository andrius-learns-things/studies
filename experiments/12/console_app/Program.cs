using System;
using System.Collections.Generic;

namespace console_app
{
    class Item
    {
        public string Name { get; set; }

        public List<Item> Children { get; set; }

        public string TraverseNames()
        {
            var result = this.Name.ToString();

            if (this.Children != null && this.Children.Count > 0)
            {
                foreach (var child in this.Children)
                {
                    result += child.TraverseNames();
                }
            }

            return result;
        }
    }

    class MainClass
    {
        static void Main(string[] args)
        {
            var r = new Item()
            {
                Name = "A",
                Children = new List<Item>() {
                    new Item() { Name = "B"},
                    new Item() { Name = "C"},
                }
            };

            Console.WriteLine(r.TraverseNames());

            Console.ReadLine();
        }
    }
}
