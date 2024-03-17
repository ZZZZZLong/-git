//using System.Collections;
//using System.Collections.Generic;
//using UnityEngine;

//public class UIManager : Singleton<UIManager>
//{

//    private Transform _uiRoot;

//    private Dictionary<string, string> pathDict;
//    //缓存预制件
//    private Dictionary<string, GameObject> prefabDict;
//    //一打开界面的缓存字典
//    public  Dictionary<string, BasePanel> panelDict;


//    public Transform UIRoot
//    {
//        get
//        {
//            if(_uiRoot == null)
//            {
//                if (GameObject.Find("Canvas"))
//                {
//                    _uiRoot = GameObject.Find("Canvas").transform;
//                }
//                else
//                {
//                    _uiRoot = new GameObject("Canvas").transform;
                     
//                }
                
//            }
//            return _uiRoot;
//        }
//    }


//    public UIManager()
//    {
//        InitDicts();//构造函数 用于初始化一些字段和属性//使用公共构造方法是因为继承父类单例模式后没有不具备公共的无参构造函数会报错
        
        
//    }
   
//    private void InitDicts()
//    {
//        prefabDict = new Dictionary<string, GameObject>();
//        panelDict = new Dictionary<string, BasePanel>();
//        pathDict = new Dictionary<string, string>()
//        {
//            //需要新的UI就往里面加
//            {UIConst.UI_1,"UI/UI_1" },
//            {UIConst.UI_2,"UI/UI_2" },
//            {UIConst.PackagePanel,"UI/PackagePanel" }
//        };
//        //因为字典不会存入重复的键，所以使用公共构造方法 在外部实例化的话也不会累加字典里的值


//    }

//    //打开界面
//    public BasePanel OpenPanel(string name)
//    {
//        BasePanel panel = null;
//        //检查是否已经打开
//        if(panelDict.TryGetValue(name,out panel))
//        {
//            Debug.Log("界面已打开： " + name);
//            return null;
//        }
//        //检查路径是否有配置
//        string path = "";
        
//        if (!pathDict.TryGetValue(name, out path))
//        {
//            Debug.Log("界面名称有误，或未配置路径： " + name);
//            return null;
//        }
        

//        //使用缓存的预制件
//        GameObject panelPrefab = null;
//        if (!prefabDict.TryGetValue(name, out panelPrefab))
//        {
//            string realpath = "Prefabs/" + path;
//            panelPrefab = Resources.Load<GameObject>(realpath) as GameObject;
           
//            prefabDict.Add(name, panelPrefab);
            
//        }
       
//        //打开界面
//        GameObject panelObject = GameObject.Instantiate(panelPrefab , UIRoot ,false);
//        panel = panelObject.GetComponent<BasePanel>();
//        panelDict.Add(name, panel);
//        panel.OpenPanel(name);
//        return panel;

//    }
//    //关闭界面
//    public bool ClosePanel(string name)
//    {
//        BasePanel panel = null;
//        if(!panelDict.TryGetValue(name,out panel))
//        {
//            Debug.LogError("界面未打开：" + name);
//            return false;
//        }

//        panel.ClosePanel();
//        return true;
//    }


//}

//public class UIConst
//{
//    public const string PackagePanel = "PackagePanel";//在这里存储所有ui对象的名称（不同的界面） 目前需要开始界面 和菜单（暂停）界面 和背景基本界面 配置路径表 
//    public const string UI_1 = "UI_1";
//    public const string UI_2 = "UI_2";
//}

