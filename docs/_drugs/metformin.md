---
layout: default
title: Metformin
parent: 僅模型預測 (L5)
nav_order: 559
evidence_level: L5
indication_count: 5
---

# Metformin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Metformin：從第二型糖尿病到典型僵人症候群

## 一句話總結

Metformin（二甲雙胍）是香港已上市的口服降血糖藥，一般用於第二型糖尿病。
TxGNN 模型預測它可能對**典型僵人症候群 (Classic Stiff Person Syndrome)** 有效。
目前**沒有臨床試驗和文獻**支持，僅有模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明適應症文字（第二型糖尿病為一般藥理知識，非本次資料所載） |
| 預測新適應症 | 典型僵人症候群 (Classic Stiff Person Syndrome) |
| TxGNN 預測分數 | 99.45% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Metformin 在降血糖上的療效已被廣泛使用，一般認為它透過活化 AMPK 來改善胰島素敏感性。這是通用藥理知識，並非本次資料所載。

僵人症候群主要是自體免疫疾病，多與抗 GAD65 抗體有關，也常合併自體免疫性糖尿病。這可能是模型把兩者連在一起的原因之一。Metformin 的 AMPK 活化和抗發炎作用，理論上可能影響免疫或代謝路徑。

這個關聯目前只是推測，未經驗證。高圖譜分數不等於臨床證據，機轉上是否真的適用仍需文獻和實驗確認。

**同一次預測中的其他候選（皆為 L5、Hold）：**

| 排名 | 預測疾病 | 分數 | 說明 |
|------|---------|------|------|
| 2 | 局部僵硬肢症候群 (Focal Stiff Limb Syndrome) | 99.45% | 屬僵人症候群譜系，分數與第 1 名相同，可能來自共同的圖譜鄰居，不算獨立支持 |
| 3 | Opsismodysplasia | 99.40% | 罕見骨骼發育不良，與 INPPL1 (SHIP2) 變異及 PI3K/Akt 訊號有關，僅為路徑層面的假說，兒童安全性需另行評估 |
| 4 | 硫胺素反應性功能障礙症候群 (Thiamine-responsive Dysfunction Syndrome) | 99.40% | 此症候群含糖尿病，通常以硫胺素和胰島素處理。Metformin 是否影響硫胺素狀態需先查文獻，這也是潛在安全疑慮 |
| 5 | 藥物引起的局部脂肪失養症 (Drug-induced Localized Lipodystrophy) | 99.06% | 多為注射部位病變（如胰島素）。Metformin 可能間接減少胰島素用量，但不能治療局部脂肪組織變化本身 |

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Metformin 在香港共有 20 張許可證，以下列出 5 張主要許可證。資料中未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-49681 | METFORMIN BDC TAB 500MG | TRENTON-BOMA LTD |
| HK-61081 | PANFOMIN TAB 500MG | VAST RESOURCES PHARMACEUTICAL LTD |
| HK-58075 | DIABETMIN 850 TAB 850MG | HOVID LIMITED |
| HK-33714 | SIAMFORMET TAB 0.5G | KAI YUEN PHARMACEUTICAL CO |
| HK-66869 | METPHAR XR 750 EXTENDED-RELEASE TABLETS 750MG | PRIMAL CHEMICAL CO LTD |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 僅有 TxGNN 模型預測（分數 99.45%），沒有任何臨床試驗或文獻支持，證據等級為 L5。
- 缺少作用機轉資料和香港仿單的警語與禁忌，無法進行安全性篩選。

**若要推進需要：**
- 補充 Metformin 的作用機轉資料（例如查詢 DrugBank）。
- 下載並解析香港衛生署的仿單，取得警語與禁忌症。
- 檢索 Metformin 與僵人症候群（含抗 GAD65 自體免疫）的文獻，確認是否有病例報告或機轉研究。
- 確認給藥途徑與目標族群是否相容，目前該項仍待評估。
- 若後續要考慮硫胺素反應性功能障礙症候群，先查 Metformin 與硫胺素轉運或狀態的關係。

本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

