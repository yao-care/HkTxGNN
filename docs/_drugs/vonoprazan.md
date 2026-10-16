---
layout: default
title: Vonoprazan
parent: 僅模型預測 (L5)
nav_order: 941
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Vonoprazan：預測新適應症為活動性消化性潰瘍 (Active Peptic Ulcer Disease)（證據等級 L5）。原適應症：胃潰瘍、十二指腸潰瘍、食道炎、胃食道逆流症"
---

# Vonoprazan
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

# Vonoprazan：從胃潰瘍／十二指腸潰瘍到活動性消化性潰瘍

## 一句話總結

Vonoprazan 是一種鉀離子競爭性胃酸阻斷劑（P-CAB），原本用於胃潰瘍、十二指腸潰瘍、食道炎及胃食道逆流症。
TxGNN 模型預測它可能對**活動性消化性潰瘍 (Active Peptic Ulcer Disease)** 有效，但此適應症與原核准用途高度重疊，實質上屬於仿單內用途，而非真正的新適應症。
目前無臨床試驗登記，有 **18 篇文獻**可參考，其中包含系統性回顧與統合分析。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 胃潰瘍、十二指腸潰瘍、食道炎、胃食道逆流症（取自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 活動性消化性潰瘍 (Active Peptic Ulcer Disease) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L3（依本報告規則判定：無已完成的 Phase 3 RCT 登記資料，有系統性回顧／統合分析；資料庫自動評分為 L1，詳見下方說明） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Proceed with Guardrails |

> **證據等級說明：** 本次彙整資料中沒有任何臨床試驗登記，L1 的自動評分依賴文獻中的系統性回顧所摘要的 Phase 3 證據，並非直接取得的試驗資料。依判定規則，保守評為 L3，建議回頭核對原始 Phase 3 試驗。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料欄位，但從文獻可知，Vonoprazan 是首創的鉀離子競爭性胃酸阻斷劑，可抑制胃壁細胞的 H+/K+ ATP 酶（ATP4A），不需酸活化，起效快且抑酸效果持久，較不受進食時間與 CYP2C19 基因多型性影響。

活動性消化性潰瘍本質上就是已核准的胃潰瘍與十二指腸潰瘍，因此這個預測在機轉與臨床上都很合理，但嚴格來說屬於原適應症，不是真正的再利用。對於幽門螺旋桿菌相關潰瘍，更強的抑酸作用也可提高抗生素（如 amoxicillin）的穩定性與除菌效果。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下依證據強度優先列出（系統性回顧／RCT 優先）。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38345252](https://pubmed.ncbi.nlm.nih.gov/38345252/) | 2024 | 系統性回顧／網絡統合分析 | Am J Gastroenterol | 比較 P-CAB 與 PPI 治療 C/D 級食道炎的療效與安全性 |
| [28988197](https://pubmed.ncbi.nlm.nih.gov/28988197/) | 2018 | RCT | Gut | 長期 NSAID 治療下，Vonoprazan 預防潰瘍復發，與 lansoprazole 相比不劣 |
| [28267236](https://pubmed.ncbi.nlm.nih.gov/28267236/) | 2017 | RCT | Dig Endosc | 評估 Vonoprazan 對內視鏡黏膜下剝離術後人工胃潰瘍的癒合效果 |
| [39156336](https://pubmed.ncbi.nlm.nih.gov/39156336/) | 2024 | Review | Cureus | 全面回顧 Vonoprazan 在胃酸相關疾病（GERD、消化性潰瘍、幽門螺旋桿菌）的療效與安全性 |
| [26369775](https://pubmed.ncbi.nlm.nih.gov/26369775/) | 2016 | Review | Clin Pharmacokinet | 說明藥物動力學與藥效學，並列出日本核准的潰瘍與食道炎用法 |
| [32998241](https://pubmed.ncbi.nlm.nih.gov/32998241/) | 2020 | Review | Pharmaceuticals | Vonoprazan 作為幽門螺旋桿菌除菌治療的潛在優勢 |
| [37066678](https://pubmed.ncbi.nlm.nih.gov/37066678/) | 2023 | 藥動／藥效研究 | Aliment Pharmacol Ther | 支持糜爛性食道炎與幽門螺旋桿菌感染的最佳 Vonoprazan 劑量 |
| [36660052](https://pubmed.ncbi.nlm.nih.gov/36660052/) | 2023 | Guideline/Review | JGH Open | 幽門螺旋桿菌感染處置 |
| [42084149](https://pubmed.ncbi.nlm.nih.gov/42084149/) | 2026 | Review | Pol Arch Intern Med | P-CAB 用於糜爛性逆流疾病與壓力性潰瘍預防 |
| [41415806](https://pubmed.ncbi.nlm.nih.gov/41415806/) | 2025 | Review | Front Microbiol | 幽門螺旋桿菌除菌治療的進展與未來方向 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68731 | VOCINTI TABLETS 10MG | 錠劑 | 許可證資料未載明 |
| HK-68732 | VOCINTI TABLETS 20MG | 錠劑 | 許可證資料未載明 |

兩張許可證均為單方、現行有效，持有廠商為 Takeda Pharmaceuticals (Hong Kong) Limited。

---

## 安全性考量

- **藥物交互作用**：本次資料僅有藥理學層面的標靶資訊（作用於胃 H+/K+ ATP 酶 ATP4A），沒有具體的藥物配對交互作用資料。
- **長期強效抑酸**：長期持續深度抑酸可能與高胃泌素血症相關，長期使用時需留意。

其餘警語與禁忌症資料缺乏，請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 活動性消化性潰瘍與 Vonoprazan 原核准的胃潰瘍／十二指腸潰瘍適應症本質相同，機轉合理，且有系統性回顧與 RCT 文獻支持；Vonoprazan 相對於 PPI 在潰瘍治療上的優勢仍有爭議。
- 沒有臨床試驗登記資料，且香港仿單的警語與禁忌症尚未取得，因此需設定防護條件。

**若要推進需要：**
- 取得香港衛生署核准的仿單，確認適應症、警語與禁忌症
- 核對原始 Phase 3 試驗，確認 Vonoprazan 對潰瘍的療效與 PPI 相比的結果
- 補充詳細的作用機轉資料
- 建立長期使用的安全性監測計畫（含高胃泌素血症）

---

## 其他預測適應症簡評

| 預測適應症 | TxGNN 分數 | 建議 | 說明 |
|-----------|-----------|------|------|
| 胃空腸吻合口潰瘍 (Gastrojejunal ulcer) | 99.97% | 研究性問題 | 吻合口潰瘍依賴胃酸，強效抑酸在機轉上合理，但現有文獻皆為間接證據，缺乏吻合口潰瘍專屬研究 |
| 消化性潰瘍穿孔 (Peptic ulcer perforation) | 99.97% | Hold | Vonoprazan 無法治療穿孔本身，僅可能用於潰瘍預防與術後抑酸，無穿孔專屬資料 |
| 食道裂孔疝 (Hiatus hernia) | 99.88% | 研究性問題 | 藥物治療的是逆流後果而非疝氣本身；現有研究價值在於病人分層（食道裂孔疝是停藥後症狀復發的預測因子） |
| 胃酸缺乏症 (Achlorhydria) | 99.86% | Hold（建議排除） | 此病為胃酸分泌缺乏，而 Vonoprazan 抑制胃酸，機轉上不適用，應視為模型的假陽性訊號 |
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

