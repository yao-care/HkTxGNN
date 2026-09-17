---
layout: default
title: Olodaterol
parent: 僅模型預測 (L5)
nav_order: 542
evidence_level: L5
indication_count: 2
---

# Olodaterol
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

# Olodaterol：從慢性阻塞性肺病（COPD）到支氣管炎（Bronchitis）

## 一句話總結

Olodaterol 是一種長效型 β2 腎上腺素受體促效劑（LABA），文獻顯示其國際上核准用途為 COPD 的長期維持性支氣管擴張治療（常與 Tiotropium 併用為固定劑量複方），但香港尚未上市，無許可證資料。TxGNN 模型預測它對**支氣管炎 (Bronchitis)** 同樣有效，目前有 **3 個臨床試驗**和 **2 篇文獻**直接支持這個方向；模型的第二預測適應症「阻塞性肺病 (Obstructive Lung Disease)」則有多達 50 個臨床試驗與 20 篇文獻佐證，其中多筆為完成的 Phase 3 RCT。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（香港未上市，無許可證資料；國際文獻顯示原用途為 COPD 長期維持治療） |
| 預測新適應症 | 支氣管炎 (Bronchitis) |
| TxGNN 預測分數 | 99.84% |
| 證據等級 | L3（僅上市後觀察性/藥物使用研究與回顧文獻，無針對「支氣管炎」的 RCT） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 Olodaterol 詳細的結構化作用機轉資料（DrugBank MOA 為資料缺口）。根據證據包內文獻，Olodaterol（商品名 Striverdi® Respimat®）是吸入型長效 β2-agonist（LABA），常與長效抗蕈毒鹼藥物 Tiotropium 併用為固定劑量複方（Spiolto®/Stiolto® Respimat®），作用機轉為刺激支氣管平滑肌 β2 受體，促使支氣管擴張。

支氣管炎與 COPD 同屬下呼吸道阻塞性疾病，兩者在氣道發炎、支氣管平滑肌痙攣的病理機轉上高度重疊。由於 Olodaterol 本身的核心藥理作用即為支氣管擴張，機轉上延伸至（急性或慢性）支氣管炎的症狀緩解具有合理性。

值得注意的是，第二預測適應症「阻塞性肺病」實質上即為 COPD——這與 Olodaterol 原本已知的核准用途高度重疊，顯示 TxGNN 在此案例中可能是辨識出既有的藥理歸類，而非發現全新的老藥新用機會。「支氣管炎」作為獨立適應症的預測，則相對更接近真正的擴展應用。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05127304](https://clinicaltrials.gov/study/NCT05127304) | N/A | 完成 | 11316 | 評估 COPD 患者起始 Tiotropium/Olodaterol 相較於 Fluticasone Furoate/Umeclidinium/Vilanterol 之醫療資源利用、成本與臨床結果 |
| [NCT03333018](https://clinicaltrials.gov/study/NCT03333018) | N/A | 完成 | 22155 | 歐洲 Aclidinium（單方及與 Formoterol 複方）新使用者之描述性藥物使用研究，含 COPD 用藥模式分析 |
| [NCT02850978](https://clinicaltrials.gov/study/NCT02850978) | N/A | 完成 | 1335 | 日本上市後監測：Tiotropium+Olodaterol 固定劑量複方於 COPD（含慢性支氣管炎、肺氣腫）患者長期安全性與有效性 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [27354040](https://pubmed.ncbi.nlm.nih.gov/27354040/) | 2016 | Review | Am J Health-Syst Pharm | 回顧 Olodaterol 之藥理學、藥動學、療效與安全性資料 |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Guideline | Basic Clin Pharmacol Toxicol | 芬蘭 COPD 穩定期診斷與藥物治療指引，涵蓋支氣管擴張劑使用建議 |

## 香港上市資訊

Olodaterol 目前未在香港取得藥品許可證（未上市），無許可證資料可供列出。

## 安全性考量

安全性資訊請參考原廠仿單。（註：TFDA 仿單警語與禁忌症資料為 **Blocking** 等級缺口，目前無法完成安全性初評 S1。）

## 結論與下一步

**決策：Hold**

**理由：**
- 支氣管炎適應症的證據僅來自上市後觀察性/藥物使用研究與回顧文獻，缺乏針對此適應症的對照試驗（RCT），證據強度僅達 L3。
- 安全性初評所需的仿單警語與禁忌症資料為 Blocking 缺口，且藥物於香港未上市、無許可證與原適應症紀錄，S1 安全性初評目前無法完成。
- 第二預測適應症（阻塞性肺病）雖有大量 Phase 3 RCT 佐證，但實質與 Olodaterol 既有 COPD 用途重疊，novelty 有限，需先釐清「支氣管炎」是否為真正具區隔性的老藥新用標的。

**若要推進需要：**
- 取得 TFDA/原廠仿單，補齊警語、禁忌症與 DDI 資料（解除 DG001 Blocking 缺口）
- 取得 DrugBank 詳細 MOA 與藥物分類資料（解除 DG002）
- 確認香港是否有引進計畫或既有許可證資訊
- 針對「支氣管炎」單一適應症檢索是否有更直接的 RCT 或對照研究證據
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

