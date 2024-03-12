using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;

public class SaveSystem : MonoBehaviour
{
    #region JSON
    public static void SaveByJson(string saveFileName, object data)
    {
        var json = JsonUtility.ToJson(data);

        var path = Path.Combine(Application.persistentDataPath,saveFileName);

        File.WriteAllText(path, json);

        
        try
        {
            Debug.Log($"³É¹¦´æµµÊý¾ÝÔÚ{path}.");

        }
        catch (System.Exception exception)
        {
            Debug.LogError($"´æµµµ½{path}Ê§°Ü.\n{exception}");
        }
    }

    public static T LoadFromJson<T>(string saveFileName)
    {
        var path = Path.Combine(Application.persistentDataPath, saveFileName);

        

        try
        {
            var json = File.ReadAllText(path);
            var data = JsonUtility.FromJson<T>(json);
            return data;
        }
        catch (System.Exception exception)
        {
            Debug.LogError($"´æµµ¶ÁÈ¡Ê§°ÜÔÚ{path}. \n{exception}");
            return default;
        }

    }

    public static void DeleteSaveFlie(string saveFileName)
    {
        var path = Path.Combine(Application.persistentDataPath, saveFileName);


        try
        {
            File.Delete(path);
        }
        catch(System.Exception exception) 
        {
            Debug.LogError($"´æµµÎ»ÖÃ´íÎó:{path}. \n{exception}");
        }


    }




    #endregion
}
