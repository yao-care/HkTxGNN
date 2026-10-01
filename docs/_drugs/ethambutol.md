---
layout: default
title: Ethambutol
parent: 僅模型預測 (L5)
nav_order: 340
evidence_level: L5
indication_count: 5
---

# Ethambutol
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

# Ethambutol：從結核病到會厭炎

## 一句話總結

Ethambutol（乙胺丁醇）是一線抗結核藥，原本用於結核病治療。
TxGNN 模型預測它可能對**會厭炎 (Epiglottitis)** 有效，但目前**沒有臨床試驗**，只有 **2 篇間接相關文獻**（皆為喉結核的報告）。
這個預測較可能反映「喉結核累及會厭」，不是新的治療機會。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 會厭炎 (Epiglottitis) |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L4（文獻僅間接涉及喉結核，無直接證據） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Ethambutol 抑制阿拉伯糖基轉移酶（arabinosyl transferase，embB），阻斷分枝桿菌細胞壁的合成。DrugBank 的作用機轉欄位目前缺資料，以上機轉來自預測理由中的說明。

這個關聯是間接的。文獻描述的是**喉結核**累及會厭，患者接受標準多藥抗結核療程，Ethambutol 只是其中一個成分。TxGNN 的高分（0.999）很可能來自知識圖譜中 Ethambutol 與結核病的連結。

對於一般急性會厭炎（例如 Hib 感染），Ethambutol 沒有抗菌作用，因此**不能視為這類疾病的老藥新用訊號**。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [14720571](https://pubmed.ncbi.nlm.nih.gov/14720571/) | 2004 | Review | The Lancet Infectious Diseases | 喉結核的綜述，資料中無摘要可供摘錄 |
| [2806495](https://pubmed.ncbi.nlm.nih.gov/2806495/) | 1989 | 病例系列（回溯性，41 例） | The European Respiratory Journal | 喉結核 41 例，好發部位依序為真聲帶、會厭、假聲帶等；患者多以 isoniazid、rifampicin、ethambutol 等藥物治療 |

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-50311 | EMB-FATOL TAB 400MG | MEKIM LTD |
| HK-50312 | EMB-FATOL TAB 100MG | MEKIM LTD |
| HK-67534 | TAMBUTOL TABLETS 400MG | SB PHARMA LIMITED |
| HK-60915 | LAMBUTOL TAB 400MG | ATLANTIC PHARMACEUTICAL LIMITED |

香港許可證資料未提供劑型與核准適應症文字，僅能從品名判斷均為錠劑。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有臨床試驗，文獻僅有 2 篇且都是喉結核相關，Ethambutol 的獨立貢獻無法與其他抗結核藥區分。
- 一般（非結核性）會厭炎的常見病原體不在 Ethambutol 的抗菌範圍內，預測分數高但缺乏生物學支持。

**若要推進需要：**
- 釐清這個預測是否只是「結核病延伸到喉部或會厭」的既有適應症，不是新適應症。
- 補齊香港仿單的警語與禁忌資料，並確認 DrugBank 的作用機轉。
- 若日後聚焦結核性病灶，需說明 Ethambutol 的安全性（如視神經炎、依腎功能調整劑量）。

**其他預測適應症的參考：**
- 腹膜炎（分數 99.20%，證據 L3）有系統性回顧與病例系列，但全部是「結核性腹膜炎」的四藥合併療法，同樣屬於既有適應症的延伸。
- 喉炎（L4）也僅涉及結核性或分枝桿菌感染。
- 腦膜炎雙球菌感染與感染性中耳炎（皆 L5）沒有任何臨床試驗或文獻支持。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

