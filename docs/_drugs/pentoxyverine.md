---
layout: default
title: Pentoxyverine
parent: 僅模型預測 (L5)
nav_order: 666
evidence_level: L5
indication_count: 2
---

# Pentoxyverine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Pentoxyverine：從鎮咳用途到急性喉咽炎

## 一句話總結

Pentoxyverine 在香港以咳嗽糖漿和錠劑等形式上市，屬於鎮咳藥。
TxGNN 模型預測它可能對**急性喉咽炎 (Acute Laryngopharyngitis)** 有效。
目前**沒有任何臨床試驗或文獻**支持，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 急性喉咽炎 (Acute Laryngopharyngitis) |
| TxGNN 預測分數 | 99.59% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

> 備註：許可證資料未載明核准適應症，原適應症欄位因此省略。鎮咳用途是依藥物類別與產品名稱（咳嗽糖漿）推斷。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Pentoxyverine 是已上市的鎮咳藥，咳嗽是急性喉咽炎的常見症狀。若兩者確有關聯，較可能是**緩解咳嗽症狀**，而不是治療發炎或感染本身。這是一般醫學常識的推論，輸入資料中沒有證據支持。

0.996 的高分可能只反映知識圖譜中，藥物與咳嗽、上呼吸道相關節點距離接近，不代表經過驗證的療效。

第二順位的預測是**鼻腔疾病 (Nasal Cavity Disease)**，分數 99.57%，同樣沒有臨床試驗或文獻。這個疾病名稱過於籠統，無法建立可信的機轉關聯，不建議優先投入。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

列出 5 張主要許可證，共 20 張。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-67441 | TOCOLIN TABLETS 30MG | WELLDONE PHARMACEUTICALS LIMITED |
| HK-51081 | CARBETAN F.C. TAB 30MG | HITPHARM PHARMACEUTICAL CO LTD |
| HK-47194 | HONIL COUGH SYRUP | MEYER PHARMACEUTICALS LTD |
| HK-61559 | COUGHTON COUGH SYRUP | MEYER PHARMACEUTICALS LTD |
| HK-46568 | TUSSEDIN COUGH SYRUP | MARCHING PHARMACEUTICAL LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前只有模型預測，沒有臨床試驗、文獻或機轉資料佐證，證據等級為 L5。
- 即使關聯成立，也可能只是症狀緩解，不是新的治療適應症。
- 安全性資料缺漏，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊警語與禁忌症。
- 補充 DrugBank 的作用機轉資料，評估與急性喉咽炎的機轉關聯。
- 檢索 PubMed 與 ClinicalTrials.gov，確認是否有鎮咳藥用於急性喉咽炎的研究。
- 釐清臨床目標是緩解咳嗽症狀，還是治療疾病本身。

---
*本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

