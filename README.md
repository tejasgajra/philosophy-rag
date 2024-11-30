# Approach - Raw approach
1. Research about the rag workflow
2. convert pdf to text
3. add the text to qdrant vector db
4. api which takes user query searches the vector the db
5. sends the top 10 search results to llm 
6. llm then summarizes the results

#Approach 2 - Use langchain
