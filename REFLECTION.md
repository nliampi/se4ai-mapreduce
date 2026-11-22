# Reflection

Name: Nipat Liampisan

Answer each question in 2–3 sentences.

**1. In Task 1, what did the shuffle do with the pairs your mapper produced? Why can the reducer only run once all mappers have finished?**

> The shuffle groups the values by keys that the mappers produced. The reducer can only run once all mappers have finished because the reducer needs all the values of associated per image to calculate the total image views. If it doesn't wait for map to finish then it will return the incorrect sum. 

**2. In Task 3, why did the original job give different answers with 1 and 4 workers? Why does moving the de-duplication into the reducer fix it, whatever the number of workers or partitions?**

> The original job gives different answers in 1 and 4 workers, because the line already_sent = set() exists in each worker. This means that each worker will get a different mapping depending on which pages it contains. When deduplication is moved to the reducer this issue is resolved because all the htmls are now grouped together. The workers and partitions now has a mapper that is stateless and return all htmls without any side effects.  

**3. The photo service from the lecture releases a new object-detection model and must re-tag 4 trillion stored photos. Which part of that job is the map step, is there a reduce step, and why would you run the computation on the machines that store the photos?**

> The object detection model is the mapping step. In this step, each object is mapped to the image. Object is the key and image name is the value. The reduce step is combining all the images associated with the object into a list. The computation should be run on the machine that stores the photos, because sending the photos over the network will be costly and slow.
