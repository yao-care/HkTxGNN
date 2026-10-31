---
layout: default
title: Sulfadiazine
parent: 僅模型預測 (L5)
nav_order: 838
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-31
description: "Sulfadiazine：預測新適應症為肺囊蟲症 (Pneumocystosis)（證據等級 L4）。原適應症：弓形蟲症（Toxoplasmosis）、潰瘍性結腸炎、發炎性腸道疾病、脈絡視網膜炎等"
monitor_inn: "SULFADIAZINE"
predicted_indications: ["pneumocystosis", "punctate epithelial keratoconjunctivitis"]
---

# Sulfadiazine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Sulfadiazine：從弓形蟲症到肺囊蟲症（Pneumocystosis）
{: .text-alpha }

## 一句話總結

Sulfadiazine 是一種磺胺類抗菌藥物，原本用於弓形蟲症、潰瘍性結腸炎、脈絡視網膜炎等適應症。
TxGNN 模型預測它可能對**肺囊蟲症 (Pneumocystosis)** 有效，
目前**沒有臨床試驗**，僅有 **19 篇文獻**（多為回顧性文章與病例報告，且未直接證明 sulfadiazine 單獨用於肺囊蟲症）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 弓形蟲症（Toxoplasmosis）、潰瘍性結腸炎、發炎性腸道疾病、脈絡視網膜炎等（香港許可證未載明核准適應症文字） |
| 預測新適應症 | 肺囊蟲症 (Pneumocystosis) |
| TxGNN 預測分數 | 0.9939 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張 |
| 建議決策 | Hold（列為研究問題，待補充證據） |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，sulfadiazine 屬於磺胺類藥物，此類藥物會抑制葉酸合成路徑中的二氫蝶酸合成酶（dihydropteroate synthase, DHPS）。

肺囊蟲（*Pneumocystis jirovecii*）同樣依賴這條葉酸合成路徑。磺胺類藥物（尤其是 sulfamethoxazole 與 trimethoprim 的複方）已是肺囊蟲肺炎的標準治療，因此在機轉上具有合理性。此外，弓形蟲症與肺囊蟲肺炎常見於 AIDS 等免疫不全患者，臨床上常同時出現，也是模型分數偏高的可能原因。

需要留意的是，現有文獻主要談的是弓形蟲感染、AIDS 相關伺機性感染與 TMP-SMX 的安全性，並沒有直接證據顯示 sulfadiazine 單獨用於肺囊蟲症有效。高預測分數很可能來自與 sulfamethoxazole 的類別相似性。另有文獻指出 *P. jirovecii* 的 DHPS 基因突變會造成磺胺類藥物交叉抗藥，這也是需要考慮的限制。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

下表列出較相關的文獻（本次整理的文獻多為回顧性文章或病例報告，無 RCT）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Review | American Family Physician | 抗寄生蟲藥物回顧；quinine-pyrimethamine-sulfadiazine 用於抗氯喹惡性瘧，TMP-SMX 用於肺囊蟲肺炎 |
| [9097375](https://pubmed.ncbi.nlm.nih.gov/9097375/) | 1997 | Review | Seminars in Respiratory Infections | 免疫不全患者的弓形蟲肺炎 |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Review | Drugs | 全身性原蟲感染（含肺囊蟲、弓形蟲）的治療與預防 |
| [2011633](https://pubmed.ncbi.nlm.nih.gov/2011633/) | 1991 | Review | Primary Care | AIDS 相關寄生蟲疾病，含肺囊蟲肺炎與腦部弓形蟲症 |
| [29604970](https://pubmed.ncbi.nlm.nih.gov/29604970/) | 2018 | Review | Handbook of Clinical Neurology | HIV 患者中樞神經系統弓形蟲感染 |
| [1344647](https://pubmed.ncbi.nlm.nih.gov/1344647/) | 1992 | Review | Bailliere's Clinical Neurology | HIV 疾病中樞神經系統伺機性感染的臨床面向 |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Review | Clinical Pharmacy | AIDS 感染性併發症的治療，肺囊蟲肺炎為最常見 |
| [9562233](https://pubmed.ncbi.nlm.nih.gov/9562233/) | 1998 | Review | Int J Clin Pharmacol Ther | 抗感染藥物腎毒性，含磺胺類結晶沉積的阻塞性效應 |
| [7909657](https://pubmed.ncbi.nlm.nih.gov/7909657/) | 1994 | Review | Annals of Internal Medicine | AIDS 相關伺機性感染處置的新進展 |
| [2645082](https://pubmed.ncbi.nlm.nih.gov/2645082/) | 1989 | 未分類 | Clinical Pharmacy | Pyrimethamine-sulfadiazine 用於 AIDS 患者的肺囊蟲肺炎與弓形蟲症（無摘要） |

## 香港上市資訊

香港共有 20 張有效的單一成分許可證，以下列出 5 張主要許可證。資料中未記載劑型與核准適應症文字。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-33558 | SULFAPRIM S INJECTABLE SUSP (VET) | 未載明 | 未載明（獸用注射懸液） |
| HK-40105 | PAFULIMA CREAM | 未載明（乳膏） | 未載明 |
| HK-40101 | SINOCORT CREAM | 未載明（乳膏） | 未載明 |
| HK-18999 | CARRIDERM DERMATOLOGICAL CREAM | 未載明（乳膏） | 未載明 |
| HK-19339 | FUOGORTE-F CREAM | 未載明（乳膏） | 未載明 |

其餘 15 張許可證中，除第 1 張為獸用注射懸液外，其餘多為外用乳膏製劑。

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自知識圖譜，非仿單文字）：
  - 血液相關：血液疾病、血小板減少、嗜中性球減少、白血球減少、顆粒球缺乏症、貧血（含巨球性貧血、葉酸缺乏性貧血）、再生不良性貧血、G6PD 缺乏症
  - 代謝相關：紫質症（含遺傳性紫質症、紫質代謝疾病）、慢性代謝疾病如胱胺酸尿症、半乳糖血症、肝醣儲積症、乙醯化慢者
  - 器官相關：腎臟疾病、肝臟疾病、膽囊疾病、泌尿道阻塞、輸尿管膿腫
  - 其他：氣喘（含內因性、過敏性）、重複感染
- **藥物交互作用**：共查得 82 筆交互作用，已列出者皆為中度，主要為降血糖藥物（可能增強降血糖作用），例如：
  - 磺醯脲類：Chlorpropamide、Glimepiride、Glipizide、Glyburide、Tolazamide
  - 格列奈類：Repaglinide、Nateglinide
  - 多種胰島素製劑
  - 其他：Balsalazide、Picosulfuric acid、Naltrexone

其他警語與仿單禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 肺囊蟲症的預測僅有模型分數與機轉上的類別推論支持（L4），沒有臨床試驗，也沒有直接顯示 sulfadiazine 單獨用於肺囊蟲症的文獻；現有標準治療是 TMP-SMX。
- 次要預測「點狀上皮角膜結膜炎」（分數 0.9936，L5）沒有任何臨床試驗或文獻，且機轉上缺乏合理連結，可能只是反映與眼部適應症的網絡鄰近性，不建議推進。

**若要推進需要：**
- 取得 sulfadiazine 的詳細作用機轉資料與香港仿單的警語、禁忌資訊
- 針對 sulfadiazine 用於肺囊蟲症（單用或合併 pyrimethamine）的直接臨床或前臨床證據進行系統性文獻檢索
- 與標準治療 TMP-SMX 比較療效與安全性，並評估 *P. jirovecii* DHPS 突變造成的抗藥性影響
- 評估血液學毒性、腎臟結晶尿與 G6PD 缺乏等高風險族群的安全性監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

