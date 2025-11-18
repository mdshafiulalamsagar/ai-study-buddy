import os
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults

# .env ফাইল থেকে API Key গুলো লোড করি
load_dotenv()

# Tavily Search টুলটি পরীক্ষা করা হচ্ছে
print("Tavily Search টুল পরীক্ষা করা হচ্ছে...")

try:
    # LangChain নিজে থেকেই .env ফাইল থেকে "TAVILY_API_KEY" খুঁজে নেবে
    # k=3 মানে হলো আমরা সেরা ৩টি সার্চ রেজাল্ট দেখতে চাই
    search_tool = TavilySearchResults(k=3)

    # চলুন টুলটিকে একটি সহজ জিনিস সার্চ করতে বলি
    search_query = "What is the latest news about Python programming language?"
    results = search_tool.invoke(search_query)

    # সার্চ রেজাল্টগুলো প্রিন্ট করি
    print(f"\n--- '{search_query}'-এর জন্য Tavily-এর সার্চ রেজাল্ট ---")

    # Tavily রেজাল্টগুলোকে একটি লিস্ট হিসেবে দেয়
    for res in results:
        print(f"URL: {res.get('url')}")
        print(f"Content: {res.get('content')[:150]}...") # কন্টেন্ট খুব লম্বা হতে পারে, তাই প্রথম ১৫০ অক্ষর দেখাচ্ছি
        print("------------------------")

except Exception as e:
    print("\n--- একটি সমস্যা হয়েছে! ---")
    print(f"Error: {e}")
    print("\nদয়া করে চেক করুন:")
    print("১. আপনার .env ফাইলে 'TAVILY_API_KEY' ঠিকভাবে সেট করা আছে কি না।")
    print("২. আপনার ইন্টারনেট কানেকশন চালু আছে কি না।")