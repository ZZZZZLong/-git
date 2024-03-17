//using System.Collections;
//using System.Collections.Generic;
//using UnityEngine;
//using UnityEngine.UI;
//using DG.Tweening;

//public class UI_2 : BasePanel
//{
//    public Button back;

//    public override void OpenPanel(string name)
//    {
        
//        base.OpenPanel(name);
//        CanvasGroup canvasGroup = GetComponent<CanvasGroup>();
//        canvasGroup.alpha = 0.0f;
//        if (canvasGroup != null)
//        {
//            DOTween.To(() => canvasGroup.alpha, x => canvasGroup.alpha = x, 1f, 1);
//        }
//        else
//        {
//            return;
//        }
       
//    }

//    public override void ClosePanel()
//    {
        
//        CanvasGroup canvasGroup = GetComponent<CanvasGroup>();
//        if (canvasGroup != null)
//        {
//            DOTween.To(() => canvasGroup.alpha, x => canvasGroup.alpha = x, 0, 1).OnComplete(
//            () =>
//            {
//                base.ClosePanel();
//            }
//            );
//        }
//        else
//        {
//            return;
//        }
        
//    }


//    public void Back()
//    {
//        print("¹Ø±Õui2");
//        UIManager.Instance.ClosePanel(UIConst.UI_2); 
//    }


//}
