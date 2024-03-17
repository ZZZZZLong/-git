using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerData : MonoBehaviour
{
    [SerializeField] string playerName = "Player Name";
    [SerializeField] int level = 0;
    [SerializeField] int coin = 0;


    const string PLAYER_DATA_KEY = "PlayerData";
    const string PLAYER_DATA_FILE_NAME = "ZLONG.ZS";


    public string Name => playerName;//Ö»¶Á

    public int Level => level;
    public int Coin => coin;

    public Vector3 Position => transform.position;


    [System.Serializable]
    class SaveData
    {
        public string playerName;

        public int playerLevel;

        public int playerCoin;

        public Vector3 playerPosition;


    
    }


    public void Save()
    {
        SaveByJson();
    }
    public void Load()
    {
        LoadFromJson();
    }



    void SaveByJson()
    {
        SaveSystem.SaveByJson(PLAYER_DATA_FILE_NAME, SavingData());
        //SaveSystem.SaveByJson($"{System.DateTime.Now:yyyy.dd.M HH-mm-ss}ZLONG.ZS", SavingData());
    }

    void LoadFromJson()
    {
        var saveData = SaveSystem.LoadFromJson<SaveData>(PLAYER_DATA_FILE_NAME);

        LoadData(saveData);
    }


    SaveData SavingData()
    {
        var saveData = new SaveData();

        saveData.playerName = playerName;
        saveData.playerLevel = level;
        saveData.playerCoin = coin;
        saveData.playerPosition = transform.position;

        return saveData;

    }

    void LoadData(SaveData saveData)
    {
        playerName = saveData.playerName;
        level = saveData.playerLevel;
        coin = saveData.playerCoin;
        transform.position = saveData.playerPosition;
    }


    [UnityEditor.MenuItem("Developer/Delete Player Data Prefs")]
    public static void DeletePlayerDataPrefs()
    {
        PlayerPrefs.DeleteKey(PLAYER_DATA_KEY);
    }

    [UnityEditor.MenuItem("Developer/Delete Player Data Save Flie")]
    public static void DeletePlayerDataSaveFile()
    {
        SaveSystem.DeleteSaveFlie(PLAYER_DATA_FILE_NAME);
    }



}
