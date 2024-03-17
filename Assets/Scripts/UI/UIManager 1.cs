//using System.Collections;
//using System.Collections.Generic;
//using UnityEngine;

//public class UIManager : Singleton<UIManager>
//{

//    private Transform _uiRoot;

//    private Dictionary<string, string> pathDict;
//    //����Ԥ�Ƽ�
//    private Dictionary<string, GameObject> prefabDict;
//    //һ�򿪽���Ļ����ֵ�
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
//        InitDicts();//���캯�� ���ڳ�ʼ��һЩ�ֶκ�����//ʹ�ù������췽������Ϊ�̳и��൥��ģʽ��û�в��߱��������޲ι��캯���ᱨ��
        
        
//    }
   
//    private void InitDicts()
//    {
//        prefabDict = new Dictionary<string, GameObject>();
//        panelDict = new Dictionary<string, BasePanel>();
//        pathDict = new Dictionary<string, string>()
//        {
//            //��Ҫ�µ�UI���������
//            {UIConst.UI_1,"UI/UI_1" },
//            {UIConst.UI_2,"UI/UI_2" },
//            {UIConst.PackagePanel,"UI/PackagePanel" }
//        };
//        //��Ϊ�ֵ䲻������ظ��ļ�������ʹ�ù������췽�� ���ⲿʵ�����Ļ�Ҳ�����ۼ��ֵ����ֵ


//    }

//    //�򿪽���
//    public BasePanel OpenPanel(string name)
//    {
//        BasePanel panel = null;
//        //����Ƿ��Ѿ���
//        if(panelDict.TryGetValue(name,out panel))
//        {
//            Debug.Log("�����Ѵ򿪣� " + name);
//            return null;
//        }
//        //���·���Ƿ�������
//        string path = "";
        
//        if (!pathDict.TryGetValue(name, out path))
//        {
//            Debug.Log("�����������󣬻�δ����·���� " + name);
//            return null;
//        }
        

//        //ʹ�û����Ԥ�Ƽ�
//        GameObject panelPrefab = null;
//        if (!prefabDict.TryGetValue(name, out panelPrefab))
//        {
//            string realpath = "Prefabs/" + path;
//            panelPrefab = Resources.Load<GameObject>(realpath) as GameObject;
           
//            prefabDict.Add(name, panelPrefab);
            
//        }
       
//        //�򿪽���
//        GameObject panelObject = GameObject.Instantiate(panelPrefab , UIRoot ,false);
//        panel = panelObject.GetComponent<BasePanel>();
//        panelDict.Add(name, panel);
//        panel.OpenPanel(name);
//        return panel;

//    }
//    //�رս���
//    public bool ClosePanel(string name)
//    {
//        BasePanel panel = null;
//        if(!panelDict.TryGetValue(name,out panel))
//        {
//            Debug.LogError("����δ�򿪣�" + name);
//            return false;
//        }

//        panel.ClosePanel();
//        return true;
//    }


//}

//public class UIConst
//{
//    public const string PackagePanel = "PackagePanel";//������洢����ui��������ƣ���ͬ�Ľ��棩 Ŀǰ��Ҫ��ʼ���� �Ͳ˵�����ͣ������ �ͱ����������� ����·���� 
//    public const string UI_1 = "UI_1";
//    public const string UI_2 = "UI_2";
//}

