---
layout: default
title: Entacapone
parent: 僅模型預測 (L5)
nav_order: 317
evidence_level: L5
indication_count: 10
---

# Entacapone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Entacapone：從帕金森氏症到 PLA2G6 相關神經退化症

## 一句話總結

Entacapone 是周邊 COMT 抑制劑，臨床上用來延長左旋多巴（levodopa）的作用，輔助治療帕金森氏症。
TxGNN 模型預測它可能對 **PLA2G6 相關神經退化症 (PLA2G6-associated neurodegeneration)** 有效。
目前**沒有任何臨床試驗或文獻**支持，僅有模型預測，屬於假說階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明適應症；依藥理分類為帕金森氏症輔助治療 |
| 預測新適應症 | PLA2G6 相關神經退化症 (PLA2G6-associated neurodegeneration) |
| TxGNN 預測分數 | 99.76% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 10 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。已知 Entacapone 是周邊 COMT 抑制劑，可減緩左旋多巴在周邊的代謝，延長其療效。在帕金森氏症中，它是左旋多巴的輔助用藥。

PLA2G6 相關神經退化症的部分表型（例如肌張力不全合併帕金森症狀）涉及多巴胺功能失調。因此從症狀治療的角度，延長左旋多巴效果在理論上說得通。

不過兩者之間**沒有直接的機轉連結**。Entacapone 只能改善多巴胺不足所致的症狀，無法改變疾病本身的病程。這個高分預測目前只是計算結果，缺乏任何實際研究佐證。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

香港共有 10 張許可證，以下列出 5 張主要許可證。資料中未提供劑型與核准適應症。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-64723 | ENPON TABLETS 200MG | Chemillennium International (HK) Limited |
| HK-44960 | COMTAN TAB 200MG | Lotus Pharmaceutical HK Limited |
| HK-66936 | Levodopa/Carbidopa/Entacapone Teva Tablets 100mg/25mg/200mg | Teva Pharmaceutical Hong Kong Limited |
| HK-66937 | Levodopa/Carbidopa/Entacapone Teva Tablets 200mg/50mg/200mg | Teva Pharmaceutical Hong Kong Limited |
| HK-52081 | STALEVO 100/25/200MG TAB | Lotus Pharmaceutical HK Limited |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測只有模型分數，沒有臨床試驗或文獻，證據等級為 L5，機轉上也沒有直接關聯。
- 香港衛生署仿單的警語與禁忌資料尚未取得，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌症，完成安全性篩選。
- 補齊 DrugBank 的作用機轉資料，重新評估與 PLA2G6 相關神經退化症的機轉關聯。
- 針對 COMT 抑制劑用於 PLA2G6 相關神經退化症（尤其是肌張力不全合併帕金森症狀的表型）做文獻回顧。
- 確認實際的給藥途徑與劑型是否適用於目標族群。

**其他預測適應症：**
此次預測清單中，「青少年型帕金森症 (paralysis agitans, juvenile, of Hunt)」與「路易氏體失智症 (Lewy body dementia)」被標為「Research Question」。這兩者與帕金森氏症的機轉較接近，值得優先做文獻回顧。但兩者目前同樣沒有直接的療效證據。

---

*本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

