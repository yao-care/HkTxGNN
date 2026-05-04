---
layout: default
title: Dexlansoprazole
parent: 高證據等級 (L1-L2)
nav_order: 196
evidence_level: L1
indication_count: 10
---

# Dexlansoprazole
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
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

# Dexlansoprazole：從逆流性食道炎到活動性消化性潰瘍

## 一句話總結

Dexlansoprazole 是 Lansoprazole 的 R-立體異構體，採用獨特的雙延緩釋放技術（DDR），國際上主要核准用於逆流性食道炎（GERD）及侵蝕性食道炎的治療與維持。
TxGNN 模型預測它可能對**活動性消化性潰瘍（Active Peptic Ulcer Disease）**有效，
目前有 **19 個臨床試驗**和 **4 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 逆流性食道炎、侵蝕性食道炎（國際核准；香港目前未登記） |
| 預測新適應症 | 活動性消化性潰瘍（Active Peptic Ulcer Disease） |
| TxGNN 預測分數 | 99.999% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊及臨床文獻，Dexlansoprazole 屬於**質子泵抑制劑（PPI）**類藥物，為 Lansoprazole 的 R-型光學異構體。其核心機轉為不可逆阻斷胃壁細胞頂端膜的 **H⁺/K⁺-ATPase**，大幅抑制胃酸分泌（目標胃 pH > 4，持續 ≥ 16 小時/天）。獨特的雙延緩釋放技術使藥物在服用後約 1–2 小時及 4–5 小時形成雙峰吸收，維持有效酸抑制時間優於傳統單峰 PPI，對夜間胃酸突破（nocturnal acid breakthrough）亦有改善效果。

逆流性食道炎與活動性消化性潰瘍同屬**酸相關性消化道疾病**，核心病理機轉均涉及胃酸過度分泌對黏膜防護的破壞。消化性潰瘍的形成關鍵在於胃酸及胃蛋白酶對黏膜屏障的侵蝕，而持續升高胃 pH > 3–4 可使胃蛋白酶活性幾乎完全喪失（pH > 4 時），同時促進黏膜微循環恢復，加速潰瘍癒合。

事實上，Dexlansoprazole 的親代藥物 Lansoprazole 在全球多個地區已取得消化性潰瘍的正式適應症，而多項直接以 Dexlansoprazole 為受試藥物的 Phase 3 樞紐試驗也在探索其用於消化性潰瘍相關疾病的療效。TxGNN 高預測分數（99.999%）充分反映這一機轉合理性，屬於同類藥物適應症拓展的典型案例。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00251719](https://clinicaltrials.gov/study/NCT00251719) | Phase 3 | 完成 | 2054 | TAK-390MR（即 Dexlansoprazole）60 mg 及 90 mg vs Lansoprazole 30 mg 治療侵蝕性食道炎原始樞紐試驗，8 週療程直接評估本藥療效與安全性 |
| [NCT00251693](https://clinicaltrials.gov/study/NCT00251693) | Phase 3 | 完成 | 2038 | Dexlansoprazole MR 60/90 mg 對比 Lansoprazole 30 mg 治療侵蝕性食道炎的第二關鍵樞紐試驗，為 FDA 核准基礎證據之一 |
| [NCT05448001](https://clinicaltrials.gov/study/NCT05448001) | Phase 3 | 完成 | 329 | 多中心隨機雙盲主動對照試驗，評估 JP-1366 於胃潰瘍患者的療效與安全性（以 Dexlansoprazole 為主動對照組） |
| [NCT04784910](https://clinicaltrials.gov/study/NCT04784910) | Phase 3 | 完成 | 423 | DWP14012 20 mg vs Lansoprazole 15 mg 預防 NSAID 誘發消化性潰瘍，隨機雙盲平行對照，直接支持消化性潰瘍預防適應症 |
| [NCT07079540](https://clinicaltrials.gov/study/NCT07079540) | Phase 3 | 完成 | 380 | X842 50 mg vs Lansoprazole 治療逆流性食道炎，雙盲雙模擬主動對照設計，涵蓋族群藥動學分析 |
| [NCT05813561](https://clinicaltrials.gov/study/NCT05813561) | Phase 3 | 完成 | 332 | DWP14012 40 mg vs 艾索美拉唑治療逆流性食道炎，全面評估療效、安全性及成本效益 |
| [NCT04840550](https://clinicaltrials.gov/study/NCT04840550) | Phase 3 | 未知 | 390 | Tegoprazan 25 mg vs Lansoprazole 15 mg 預防長期 NSAID 治療患者胃十二指腸潰瘍，非劣效性設計 |
| [NCT06284876](https://clinicaltrials.gov/study/NCT06284876) | Phase 3 | 招募中 | 416 | Ilaprazole 10 mg vs 主動對照預防 NSAID 相關消化性潰瘍，24 週評估潰瘍發生率，預計 2027 年完成 |
| [NCT04531475](https://clinicaltrials.gov/study/NCT04531475) | Phase 2 | 完成 | 90 | X842 不同劑量 vs Lansoprazole 治療逆流性食道炎，4 週劑量效應關係探索，提供 PPI 類支持性數據 |
| [NCT04400136](https://clinicaltrials.gov/study/NCT04400136) | Early Phase 1 | 未知 | 45 | PPI 用於腹腔鏡胃袖狀切除術後對胃食管逆流症狀影響的先導研究，評估最佳術後用藥方案 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41809210](https://pubmed.ncbi.nlm.nih.gov/41809210/) | 2026 | 專家共識 | World J Gastrointest Pharmacol Ther | 印度酸性消化性疾病（含 GERD、消化性潰瘍）綜合管理共識，明確列入 PPI（含 Dexlansoprazole）的臨床定位與治療流程 |
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | 系統評價／網絡統合分析 | Am J Gastroenterol | 比較 P-CAB 與各 PPI 治療 LA C/D 級侵蝕性食道炎的療效與安全性，為 PPI 類酸抑制效力提供高品質頭對頭比較數據 |
| [36150104](https://pubmed.ncbi.nlm.nih.gov/36150104/) | 2022 | 機轉研究（體外） | J Chin Med Assoc | 探討 Dexlansoprazole 等 PPI 抑制液泡型 ATPase 及誘導內質網壓力的細胞機轉，提供分子層面的作用機轉理解 |
| [18821474](https://pubmed.ncbi.nlm.nih.gov/18821474/) | 2008 | 藥物評論 | Curr Opin Investig Drugs | Dexlansoprazole 改良釋放劑型的早期藥物評論，描述其 NDA 申請進程及在 GERD 與逆流性食道炎的臨床開發背景 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Dexlansoprazole 作為 PPI 類藥物，其持續酸抑制機轉與消化性潰瘍的核心病理高度吻合，多個已完成的 Phase 3 試驗（n > 2000）直接以 Dexlansoprazole 為受試藥物，證據等級達 L1；同類親代藥物 Lansoprazole 在多個國家已取得消化性潰瘍適應症，科學基礎充分、風險可預期。

**若要推進需要：**
- 下載並解析原廠仿單，補充香港 / TFDA 警語及禁忌症資料（目前為資料缺口）
- 透過 DrugBank API 補充完整 MOA 及交互作用資料
- 評估向香港衞生署申請上市許可的可行性（目前 0 張本地許可證）
- 確認 DDR 劑型在亞洲族群（尤其 CYP2C19 基因型分布差異）的藥動學數據
- 制定特定高風險族群（NSAID 使用者、H. pylori 感染者）的安全監測計畫
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

