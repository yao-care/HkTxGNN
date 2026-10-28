---
layout: default
title: Ethambutol
parent: 僅模型預測 (L5)
nav_order: 345
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Ethambutol：預測新適應症為會厭炎 (Epiglottitis)（證據等級 L4）。原適應症：肺結核 (Pulmonary tuberculosis)"
monitor_inn: "Ethambutol"
predicted_indications: ["epiglottitis", "laryngitis", "meningococcal infection", "peritonitis", "infectious otitis media"]
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

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Ethambutol：從肺結核到會厭炎
{: .text-alpha }

## 一句話總結

Ethambutol 是抗分枝桿菌藥物，原本用於治療肺結核。
TxGNN 模型預測它可能對**會厭炎 (Epiglottitis)** 有效，但目前**沒有臨床試驗**，僅有 **1 篇文獻**（喉結核病例系列）間接相關，屬於模型預測為主、證據薄弱的候選。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 肺結核 (Pulmonary tuberculosis) |
| 預測新適應症 | 會厭炎 (Epiglottitis) |
| TxGNN 預測分數 | 0.9990 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 4 張／共 4 張） |
| 許可證數 | 4 張（有效 4 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Ethambutol 是抗分枝桿菌藥物，一般認為其作用是抑制阿拉伯糖基轉移酶 (arabinosyl transferase)，干擾分枝桿菌細胞壁阿拉伯半乳聚糖的合成，因此在肺結核治療中已被證實有療效。

不過，這項預測的合理性有限。唯一相關的文獻是喉結核的病例系列，其中會厭是結核侵犯的部位之一。這代表 Ethambutol 只可能對「結核分枝桿菌感染會厭」有作用，而這屬於既有結核適應症在不同部位的延伸，並非真正的新適應症。

典型的細菌性會厭炎（如 H. influenzae 所致）並不在 Ethambutol 的抗菌範圍內。因此，高預測分數較可能反映「結核與喉部解剖位置」的關聯，而非真實的新療效。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [2806495](https://pubmed.ncbi.nlm.nih.gov/2806495/) | 1989 | 病例系列 | The European Respiratory Journal | 1975–1985 年共 41 例喉結核，皆有現行或既往肺結核；受侵部位依序為真聲帶、會厭、假聲帶等；病人多以包含 Ethambutol 的抗結核藥物治療 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-50311 | EMB-FATOL TAB 400MG | — | — |
| HK-67534 | TAMBUTOL TABLETS 400MG | — | — |
| HK-50312 | EMB-FATOL TAB 100MG | — | — |
| HK-60915 | LAMBUTOL TAB 400MG | — | — |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**：腎臟疾病、輸尿管積膿 (pyoureter)、痛風、糖尿病視網膜病變、糖尿病白內障、視神經炎。這些資料來自知識圖譜的藥物與疾病關聯，並非仿單文字，須以原廠仿單為準。
- **藥物交互作用**：共查得 100 筆交互作用紀錄，列出的前幾項中，中度等級包括 Metronidazole、Picosulfuric acid、Naltrexone、Rosuvastatin、Simvastatin、Tinidazole、Aluminum hydroxide。其餘多為等級未明（如 Omeprazole、Pantoprazole、Prednisone、Vancomycin 等）。

其餘警語與禁忌資料請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有臨床試驗，唯一的文獻是喉結核病例系列，屬既有結核適應症在特定部位的使用，並非新的治療機會。
- Ethambutol 對一般細菌性會厭炎無預期活性，高預測分數來自 TxGNN 模型（深度學習），可能反映模型從相關疾病間學到的相似性，並非生物學證據。

**若要推進需要：**
- 取得詳細的作用機轉資料，釐清與會厭炎的機轉關聯
- 確認會厭炎的目標族群是否僅限結核性會厭炎，若是則應歸入既有結核適應症
- 取得香港仿單的警語與禁忌資料，完成安全性篩選
- 補充 Ethambutol 對視神經的風險評估（知識圖譜已標示視神經炎相關禁忌）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

