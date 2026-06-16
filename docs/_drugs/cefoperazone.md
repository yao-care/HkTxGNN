---
layout: default
title: Cefoperazone
parent: 僅模型預測 (L5)
nav_order: 147
evidence_level: L5
indication_count: 10
---

# Cefoperazone
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

# Cefoperazone：從細菌性感染到硬化性膽管炎

## 一句話總結

Cefoperazone 是第三代頭孢菌素類廣效抗生素，用於多種細菌性感染的治療，但香港目前無上市許可、原適應症資料缺失。
TxGNN 模型以最高分預測它可能對**硬化性膽管炎 (Sclerosing Cholangitis)** 有效，
然而目前**完全無臨床試驗或文獻**支持這個方向，屬純模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 未知（香港無上市許可，原適應症資料缺失） |
| 預測新適應症 | 硬化性膽管炎 (Sclerosing Cholangitis) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Cefoperazone 的詳細作用機轉資料（MOA Data Gap）。根據藥物類別，Cefoperazone 屬第三代頭孢菌素（β-lactam 類），其藥理機轉為結合細菌青黴素結合蛋白（PBP），抑制細胞壁肽聚糖合成，進而發揮廣效殺菌作用，對多種革蘭陰性菌及部分革蘭陽性菌具活性。與 sulbactam 組合後，可進一步擴展至多重抗藥性（MDR）菌種。

硬化性膽管炎（Sclerosing Cholangitis）分為兩類：原發性硬化性膽管炎（PSC）為自體免疫/纖維化疾病，一線治療為免疫抑制或熊去氧膽酸；繼發性膽管炎則常由細菌感染或膽道阻塞所致，此情境下廣效抗生素確實用於感染控制。

TxGNN 此項預測最可能來自知識圖譜中「廣效抗生素—膽管炎（感染源）」的間接關聯，而非針對 PSC 纖維化或免疫機轉的直接療效。目前既無臨床試驗、也無任何支持性文獻，屬高度不確定的純模型預測，疑似知識圖譜假陽性。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
雖然 TxGNN 給出 99.98% 的最高分預測，但硬化性膽管炎（尤其是 PSC）為免疫介導/纖維化疾病，抗生素對其核心病理機轉無已知療效；目前完全缺乏臨床或前臨床支持證據（L5），且 Cefoperazone 在香港未上市。

**若要推進需要：**
- 補充 MOA 資料：查詢 DrugBank API 取得 Cefoperazone 完整作用機轉
- 機轉評估：釐清是否針對繼發性**細菌性**膽管炎進行定位（有別於 PSC 本身）
- 前臨床研究：需動物模型或體外數據支持抗菌以外的潛在機轉（如抗纖維化活性）
- 安全性補件：下載 TFDA 仿單 PDF 解析警語與禁忌症，完成 S1 安全性初評

---

## 附錄：全預測適應症概覽

此 Evidence Pack 共包含 10 項 TxGNN 預測，以下整理各項的臨床可行性評估：

| 排名 | 適應症 | TxGNN 分數 | 證據等級 | 決策 | 說明 |
|------|--------|-----------|---------|------|------|
| 1 | Sclerosing Cholangitis | 99.98% | L5 | Hold | 0 試驗、0 文獻；PSC 為免疫疾病，抗生素無機轉 |
| 2 | Rheumatoid Arthritis | 99.97% | L5 | Hold | 4 篇文獻均為 RA 患者併發感染，屬間接引用，非治療 RA |
| **3** | **Pneumonia** | **99.93%** | **L1** | **Proceed with Guardrails** | **2 個 RCT（含 Phase 3）、20 篇文獻；最強證據，為核心抗菌適應症** |
| 4 | Colobomatous Microphthalmia-Rhizomelic Dysplasia | 99.92% | L5 | Hold | 罕見遺傳症，抗生素無機轉，KG 假陽性 |
| 5 | Brachydactyly-Syndactyly Syndrome | 99.90% | L5 | Hold | 遺傳性骨骼發育異常，抗生素無機轉，KG 假陽性 |
| 6 | Gout | 99.83% | L5 | Hold | 尿酸代謝疾病，抗生素無機轉 |
| **7** | **Bronchitis** | **99.77%** | **L2** | **Proceed with Guardrails** | **20 篇文獻含多中心臨床試驗；下呼吸道感染合理延伸** |
| 8 | Meningococcal Infection | 99.51% | L4 | Research Question | 1 篇前驅報告；CNS 穿透率次優，需進一步評估 |
| 9 | Infectious Otitis Media | 99.50% | L4 | Research Question | 3 篇間接文獻；無口服劑型，給藥路徑不利門診使用 |
| 10 | IgG4-related Sclerosing Cholangitis | 99.48% | L5 | Hold | 免疫介導疾病，抗生素無機轉 |

> **臨床重點提示**：Pneumonia（肺炎）為此 Evidence Pack 中證據最充分的預測適應症（L1），有 RCT 數據支持 Cefoperazone/Sulbactam 用於院內肺炎（HAP/HCAP）治療，建議優先針對此適應症進行正式評估。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

