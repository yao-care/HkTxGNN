---
layout: default
title: Salbutamol
parent: 僅模型預測 (L5)
nav_order: 797
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Salbutamol：預測新適應症為支氣管炎 (Bronchitis)（證據等級 L5）。原適應症：氣喘、支氣管疾病"
monitor_inn: "SALBUTAMOL"
predicted_indications: ["papillary conjunctivitis", "nasal cavity disease", "pharyngitis", "bronchitis", "acute laryngopharyngitis"]
---

# Salbutamol
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

# Salbutamol：從氣喘與支氣管疾病到支氣管炎

## 一句話總結

Salbutamol（沙丁胺醇）是 β2 腎上腺素受器促效劑，原本用於氣喘與支氣管疾病。
TxGNN 模型預測它可能對**支氣管炎 (Bronchitis)** 有效，目前有 **8 個臨床試驗**和 **20 篇文獻**與此方向相關，但多數為間接證據，且嬰兒細支氣管炎的支氣管擴張劑療效並不一致。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 氣喘、支氣管疾病（資料庫標註；香港許可證未載明適應症文字） |
| 預測新適應症 | 支氣管炎 (Bronchitis) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L3（有系統性回顧，但無已完成的 Phase 3 RCT） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold（僅適合作為研究問題，需先釐清目標族群） |

說明：TxGNN 預測排名前 5 的疾病為乳突狀結膜炎、鼻腔疾病、咽炎、支氣管炎與急性喉咽炎。只有支氣管炎具備較完整的臨床試驗與文獻，其餘皆為證據等級 L5（僅有模型預測），建議暫緩（Hold）。本報告以支氣管炎為主軸。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就已知的藥理分類，Salbutamol 是 β2 腎上腺素受器促效劑，可放鬆支氣管平滑肌，也有研究顯示可影響黏液纖毛清除（見 PMID 6729256，慢性支氣管炎病人吸入 Salbutamol 後的黏液纖毛清除研究）。

氣喘與支氣管炎同屬阻塞性呼吸道疾病，若病人有可逆性氣道阻塞，支氣管擴張劑在機轉上有合理的作用空間。這屬於「相近適應症的延伸使用」。

不過，證據主要集中在嬰兒病毒性細支氣管炎，而 Cochrane 系統性回顧（PMID 24937099）與相關指引指出，支氣管擴張劑的效益有限或不一致，一般不建議常規使用。成人或慢性支氣管炎的現代證據在目前資料中並不充分。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00114478](https://clinicaltrials.gov/study/NCT00114478) | NA | 未知 | 600 | 隨機試驗，比較腎上腺素與 Albuterol（Salbutamol）用於細支氣管炎；直接相關，但未提供結果 |
| [NCT00696540](https://clinicaltrials.gov/study/NCT00696540) | Phase 2 | 未知 | 74 | 比較高張與一般生理食鹽水作為 Salbutamol 噴霧稀釋液，用於 RSV 流行期細支氣管炎幼童 |
| [NCT00677729](https://clinicaltrials.gov/study/NCT00677729) | Phase 2 | 完成 | 81 | 吸入 3% 高張食鹽水用於嬰兒病毒性細支氣管炎，以減少住院；Salbutamol 為間接比較或併用 |
| [NCT06665711](https://clinicaltrials.gov/study/NCT06665711) | NA | 尚未招募 | 100 | 3% 高張食鹽水與 Salbutamol 比較，用於兒童細支氣管炎；尚無結果 |
| [NCT05932316](https://clinicaltrials.gov/study/NCT05932316) | NA | 未知 | 96 | 評估支氣管擴張症病人對支氣管擴張劑的反應；相關氣道疾病，非支氣管炎療效試驗 |
| [NCT03199976](https://clinicaltrials.gov/study/NCT03199976) | Phase 4 | 終止 | 80 | Tiotropium 用於幼兒早期喘鳴，Salbutamol 為隨需用藥，非研究藥物 |
| [NCT03436225](https://clinicaltrials.gov/study/NCT03436225) | Phase 1 | 未知 | 80 | 類固醇治療急性細支氣管炎，Salbutamol 非主要介入 |
| [NCT06139029](https://clinicaltrials.gov/study/NCT06139029) | Early Phase 1 | 完成 | 60 | 3% 食鹽水與類固醇噴霧比較，Salbutamol 非重點 |

另有 NCT02863835（肺移植慢性排斥的電阻抗斷層掃描診斷研究）與本適應症關聯很低，未列入上表。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [24937099](https://pubmed.ncbi.nlm.nih.gov/24937099/) | 2014 | 系統性回顧 (Cochrane) | Cochrane Database Syst Rev | 探討支氣管擴張劑用於細支氣管炎，為嬰兒急性病毒性下呼吸道感染 |
| [33893229](https://pubmed.ncbi.nlm.nih.gov/33893229/) | 2021 | 網絡統合分析 | Pediatrics | 比較急性照護中各種細支氣管炎介入的療效 |
| [36765418](https://pubmed.ncbi.nlm.nih.gov/36765418/) | 2023 | 指引 | Ital J Pediatr | 2022 義大利嬰兒細支氣管炎處置指引，以支持性照護為主 |
| [35383741](https://pubmed.ncbi.nlm.nih.gov/35383741/) | 2022 | RCT | Mymensingh Med J | 比較 3% 高張食鹽水與一般食鹽水加 Salbutamol 治療急性細支氣管炎 |
| [6229262](https://pubmed.ncbi.nlm.nih.gov/6229262/) | 1984 | 對照試驗 | Br J Clin Pharmacol | 慢性支氣管炎 20 人，噴霧 Salbutamol 與 Ipratropium 單獨及合併使用，兩者支氣管擴張效果相近，合併使用效果與持續時間更佳 |
| [1090337](https://pubmed.ncbi.nlm.nih.gov/1090337/) | 1975 | 雙盲對照試驗 | Br Med J | 支氣管炎與氣喘各 8 人，Salbutamol 與 Ipratropium 皆優於安慰劑，可改善氣道阻塞 |
| [7002574](https://pubmed.ncbi.nlm.nih.gov/7002574/) | 1980 | 交叉試驗 | Eur J Respir Dis | 慢性支氣管炎伴可逆性氣道阻塞 21 人，比較吸入 Clenbuterol 與 Salbutamol |
| [6729256](https://pubmed.ncbi.nlm.nih.gov/6729256/) | 1984 | 雙盲研究 | Respiration | 吸入 Salbutamol 對慢性支氣管炎病人黏液纖毛清除的急性影響 |
| [37167145](https://pubmed.ncbi.nlm.nih.gov/37167145/) | 2023 | 比較試驗 | Ter Arkh | 含左旋沙丁胺醇複方與含 Salbutamol 複方，用於成人急性支氣管炎的有痰咳嗽 |
| [151547](https://pubmed.ncbi.nlm.nih.gov/151547/) | 1978 | 交叉試驗 | Br J Dis Chest | 氣喘與慢性支氣管炎病人使用 Ipratropium、Salbutamol 與 Prednisolone |

---

## 香港上市資訊

香港共有 20 張有效的單方許可證。資料庫未提供劑型與核准適應症文字，以下列出 5 張主要許可證：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-02796 | VENTOLIN SOLN FOR I.V INFUSION 1MG/ML（GSK） | 靜脈輸注液 | 未提供 |
| HK-42389 | VENTOLIN ACCUHALER 200MCG（GSK） | 吸入劑 | 未提供 |
| HK-39786 | AIROMIR INHALER 100MCG/ACTUATION | 吸入劑 | 未提供 |
| HK-54460 | ASTHALIN HFA INHALER 100MCG/DOSE | 吸入劑 | 未提供 |
| HK-33864 | VANTIN TAB 4MG | 錠劑 | 未提供 |

---

## 安全性考量

- **知識圖譜標示的禁忌或需謹慎疾病**：高血壓、長 QT 症候群、癲癇、低血鉀、糖尿病與糖尿病酮酸中毒、良性前列腺增生、高眼壓與閉角型青光眼、代謝性酸中毒、心臟驟停、心臟傳導疾病、甲狀腺機能亢進（含 Graves 病）、膀胱頸阻塞、心肌缺血與冠狀動脈疾病。此為知識圖譜關聯，並非仿單原文。
- **藥物交互作用**：共查得 100 筆，以下為部分範例。
  - 中度：Acarbose、Famotidine、Epinephrine、Clarithromycin、Cisapride、Canagliflozin、Dapagliflozin、Alogliptin、Chlorpropamide 等。其中降血糖藥物與具 QT 風險的藥物值得留意。
  - 輕度：Hydrocortisone、Dexamethasone、Budesonide、Betamethasone、Beclomethasone dipropionate。

仿單的警語與禁忌資料尚未取得，詳細內容請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 支氣管炎是這個藥物最有證據支持的預測方向，但現有試驗多以細支氣管炎為主，Salbutamol 多為對照或併用，且大多缺乏結果，也沒有已完成的 Phase 3 RCT。
- 系統性回顧顯示嬰兒細支氣管炎使用支氣管擴張劑的效益有限，因此不建議直接推進為新適應症。其他四個預測疾病則僅有模型預測。

**若要推進需要：**
- 明確界定目標族群（如成人慢性支氣管炎伴可逆性氣道阻塞，或有喘鳴或異位性體質的兒童），並整理這些族群的直接證據。
- 取得 NCT00114478、NCT00696540 等試驗的結果，並重新評估 Cochrane 回顧的結論。
- 補齊原廠仿單的警語與禁忌資料，以及作用機轉資料。
- 在評估風險時，納入心血管、血鉀與血糖相關的安全性考量。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

