using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class zıplama : MonoBehaviour
{

    //public float velocity =0.2f;
    //public Rigidbody2D rb2D;
    Vector3 velocity;
    float speedAmount = 5f;
    float JumpAmount = 5f;
    
    Rigidbody2D rgb;
    
    void Start()
    {
        rgb = GetComponent<Rigidbody2D>();
    }


    


    void Update()
    {
        //if(Input.GetMouseButtonDown(0))
        //{

            //rb2D.velocity = Vector2.up * velocity;
            //}
            //float x = Input.GetAxis ("Horizontal") * velocity;
            //float y = Input.GetAxis ("Vertical") * velocity;
            //transform.Translate(x, y, 0);
        //} 
            velocity = new Vector3(Input.GetAxis("Horizontal"), 0f);
            transform.position += velocity * speedAmount * Time.deltaTime;

            if (Input.GetButtonDown("Jump") && Mathf.Approximately(rgb.velocity.y, 0))
            {
                rgb.AddForce(Vector3.up * JumpAmount, ForceMode2D.Impulse);



            }

            if (Input.GetAxisRaw("Horizontal") == -1)
            {
                transform.rotation = Quaternion.Euler(0f, 180f, 0f);



            }
            else if (Input.GetAxisRaw("Horizontal") == 1)
            {
                transform.rotation = Quaternion.Euler(0f, 0f, 0f);


            }

          

            
            
            


    }
}
