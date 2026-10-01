---
layout: default
title: Ampicillin
parent: 僅模型預測 (L5)
nav_order: 57
evidence_level: L5
indication_count: 10
---

# Ampicillin
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

# Ampicillin：從廣效抗生素到喉炎

## 一句話總結

Ampicillin 是 β-內醯胺類（青黴素類）抗生素，在香港已有多張上市許可證。
TxGNN 模型預測它可能對**喉炎 (Laryngitis)** 有效，但目前僅有 **1 個間接相關的臨床試驗**（測試的是另一種藥）和 **約 20 篇文獻**（多為病例報告與回顧），沒有直接證據。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 喉炎 (Laryngitis) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L4（僅有間接的機轉推論與零散文獻，無直接研究） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 欄位為空）。以下依 β-內醯胺類藥物的一般藥理推論：Ampicillin 會抑制青黴素結合蛋白（PBP），阻斷細菌細胞壁肽聚醣的交聯，因此對敏感細菌有殺菌作用。若喉部感染由敏感細菌引起，例如會厭炎或喉部膿瘍，理論上可能有效。

不過，急性喉炎多數由病毒引起，抗生素通常無益。指引品質評估文獻也不支持常規使用抗生素。模型給出的高分（0.9997）較可能反映知識圖譜中「上呼吸道細菌感染」這一群相鄰疾病的關聯，並非針對喉炎本身的療效訊號。

換言之，這個預測在機轉上僅適用於**細菌性**喉部感染，不適用於一般喉炎。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01406275](https://clinicaltrials.gov/study/NCT01406275) | N/A | 完成 | 363 | 日本兒童使用 Amoxicillin/Clavulanate 乾糖漿的上市後監測，適應症涵蓋咽炎、喉炎、扁桃腺炎等。屬非對照研究，藥物與 Ampicillin 不同，與喉炎的關聯僅為間接 |

---

## 文獻證據

以下文獻多為病例報告或回顧，沒有針對 Ampicillin 治療喉炎的對照試驗。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39879424](https://pubmed.ncbi.nlm.nih.gov/39879424/) | 2025 | 指引品質評估 | CoDAS | 以 AGREE II 評估喉炎與咽炎臨床指引的方法學品質 |
| [25944348](https://pubmed.ncbi.nlm.nih.gov/25944348/) | 2015 | 回溯性世代研究 | Otolaryngol Head Neck Surg | 喉切除術的併發症與圍手術期抗生素選擇有關 |
| [35923122](https://pubmed.ncbi.nlm.nih.gov/35923122/) | 2023 | 病例報告＋歷史回顧 | Ann Otol Rhinol Laryngol | 抗生素時代喉部膿瘍罕見，報告一例糖尿病控制不佳者的自發性喉膿瘍 |
| [12402494](https://pubmed.ncbi.nlm.nih.gov/12402494/) | 2002 | 病例系列 | Acta Otorrinolaringol Esp | 2 例聲門旁間隙喉膿瘍，強調需快速診斷與治療 |
| [30579693](https://pubmed.ncbi.nlm.nih.gov/30579693/) | 2019 | 病例報告 | Auris Nasus Larynx | 骨髓移植後發生喉部放線菌症 |
| [24930374](https://pubmed.ncbi.nlm.nih.gov/24930374/) | 2014 | 病例報告 | J Voice | 化療後嗜中性球低下患者的喉部放線菌症，經青黴素類長療程治療後痊癒 |
| [3977063](https://pubmed.ncbi.nlm.nih.gov/3977063/) | 1985 | 回顧（兒童會厭炎） | Anaesth Intensive Care | 161 例兒童急性會厭炎，強調氣道處置優先 |
| [2603419](https://pubmed.ncbi.nlm.nih.gov/2603419/) | 1989 | 病例系列 | West J Med | 9 例成人急性會厭炎，4 例需插管，6 例初診誤診 |
| [34986973](https://pubmed.ncbi.nlm.nih.gov/34986973/) | 2023 | 病例報告＋文獻回顧 | Auris Nasus Larynx | COVID-19 引起的急性會厭炎，可能需要緊急氣道處置 |
| [41536375](https://pubmed.ncbi.nlm.nih.gov/41536375/) | 2025 | 病例報告 | Cureus | 一名疑似哮吼（croup）的兒童，提醒對治療無反應時應重新考慮鑑別診斷 |

---

## 香港上市資訊

香港共有 20 張許可證，以下列出 5 張。資料中未記載劑型與核准適應症，需查閱衛生署仿單確認。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-10610 | A P CAP 250MG | THE UNITED LABORATORIES LTD |
| HK-63787 | AMPICILLIN POWDER FOR SOLUTION FOR INJECTION 500MG | CEUTICAL TRADING COMPANY LIMITED |
| HK-61293 | NORAPILIN POWDER FOR SOLUTION FOR IM/IV INJECTION 500MG | JINDUN PHARMA (H.K.) LIMITED |
| HK-40801 | PAMECIL FORTE FOR SYRUP 250MG/5ML | STAR MEDICAL SUPPLIES LTD |
| HK-56898 | AMPICILLIN SODIUM FOR INJ 0.5G | REGAL MEDICAL HEALTHCARE LIMITED |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級僅 L4：唯一的臨床試驗測試的是另一種藥（Amoxicillin/Clavulanate），且屬非對照的監測研究，文獻也多為個案。
- 急性喉炎以病毒性為主，抗生素不是常規建議，高預測分數較可能是圖譜相鄰關聯造成的假象。
- 若要在同類預測中找較有支持的方向，可留意**淋菌性尿道炎**（1970–80 年代有多個 Ampicillin 對照試驗，屬 L3），但那是歷史適應症，並非新用途，且現今抗藥性普遍。**慢性鼻竇炎**（L3）的證據則多為 Amoxicillin/Clavulanate，對 Ampicillin 屬間接證據。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語、禁忌與核准適應症（此為阻斷性資料缺口，目前無法進入安全性篩選）。
- 補上 Ampicillin 的作用機轉資料（DrugBank）。
- 釐清目標是「細菌性喉部感染」（例如會厭炎、喉膿瘍）還是一般喉炎，並收集這些細菌性感染中使用 Ampicillin 的直接證據。
- 評估現行病原菌的抗藥性（β-內醯胺酶）與標準療法，確認 Ampicillin 單方是否仍具臨床意義。

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

