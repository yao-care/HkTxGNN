---
layout: default
title: Entecavir
parent: 中證據等級 (L3-L4)
nav_order: 240
evidence_level: L4
indication_count: 10
---

# Entecavir
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Entecavir：從 B 型肝炎到慢性 C 型肝炎病毒感染

## 一句話總結

Entecavir 是強效鳥嘌呤核苷類似物，全球 FDA/EMA 核准用於慢性 B 型肝炎（HBV）治療，透過抑制 HBV DNA 聚合酶三個步驟（引發、逆轉錄、正股 DNA 合成）發揮抗病毒效果，IC₅₀ 低至 0.004 µM。
TxGNN 模型預測它可能對**慢性 C 型肝炎病毒感染 (chronic hepatitis C virus infection)** 有效，預測分數高達 **99.98%**，排名第 1。
然而，機轉分析顯示此預測極可能源自知識圖譜路徑混淆，目前無任何直接支持 Entecavir 治療 HCV 的臨床試驗，僅有 HBV/HCV 共感染情境下的間接證據。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性 B 型肝炎（Chronic Hepatitis B） |
| 預測新適應症 | 慢性 C 型肝炎病毒感染 (chronic hepatitis C virus infection) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Entecavir 為鳥嘌呤核苷類似物，在細胞內磷酸化後生成活性三磷酸鹽，強力抑制 HBV DNA 聚合酶的三個關鍵步驟：引發（priming）、逆轉錄（reverse transcription）以及正股 DNA 合成（plus-strand DNA synthesis）。憑借極低的 IC₅₀（0.004 µM）和高基因屏障，它是目前 HBV 治療的全球一線藥物。

然而，HCV 是一種正鏈 RNA 病毒（+ssRNA），複製依賴 NS5B RNA 依賴性 RNA 聚合酶（RdRp），與 HBV DNA 聚合酶（屬於逆轉錄酶家族）在結構和功能上完全不同。體外實驗中，Entecavir 對 HCV NS5B 無顯著抑制活性，缺乏任何直接的機轉聯結。

TxGNN 分數高（99.98%）的成因可能在於：在 HBV/HCV 共感染患者的大量臨床試驗與文獻中，Entecavir 作為 HBV 背景治療頻繁出現，導致知識圖譜在「Entecavir → HCV 相關研究情境」之間建立了強連結路徑，但這屬於共感染管理的背景角色，而非 Entecavir 本身具有直接抗 HCV 療效的證據。此為 TxGNN 知識圖譜預測典型的路徑混淆（pathway confounding）案例。

---

## 臨床試驗證據

以下為相關度最高的試驗，均涉及 HBV/HCV 共感染情境，Entecavir 均扮演 HBV 背景控制角色，無直接以 Entecavir 治療 HCV 的試驗設計：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | 已完成 | 23 | 前瞻性研究，評估 DAA 治療 HCV/HBV 共感染患者期間的 HBV 再激活發生率與危險因子；Entecavir 用於控制 HBV 成分 |
| [NCT04405011](https://clinicaltrials.gov/study/NCT04405011) | N/A | 不明 | 60 | 三臂開放標籤隨機試驗，比較 HCV/HBV 共感染患者接受 DAA 治療慢性 C 型肝炎時，預防性核苷類似物（12 週 vs 24 週 vs 不給藥）預防 HBV 再激活的效果 |

> ⚠️ 目前**無任何**以 Entecavir 為試驗藥物直接治療 HCV 感染的臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36146665](https://pubmed.ncbi.nlm.nih.gov/36146665/) | 2022 | 世代研究 | Viruses | 66 名抗 HCV 抗體陽性之慢性 HBV 患者接受核苷(酸)類似物治療期間，HCV 病毒復活現象與病毒載量動態變化觀察，為共感染管理提供依據 |
| [24773464](https://pubmed.ncbi.nlm.nih.gov/24773464/) | 2014 | 綜述 | Expert Opinion on Pharmacotherapy | HBV/HCV 共感染治療進展回顧，強調共病管理需釐清主導病毒，Entecavir 用於 HBV 成分控制 |
| [24868325](https://pubmed.ncbi.nlm.nih.gov/24868325/) | 2014 | 綜述 | World Journal of Hepatology | 肝腎移植前後 HBV 與 HCV 患者管理指引，Entecavir 為 HBV 防治首選；同時提示 HCV 治療應以干擾素或 DAA 為主 |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | 綜述 | Minerva Gastroenterologica | HBV 和 HCV 抗病毒藥物（含 Entecavir、核苷酸類似物與 DAA）對腎功能影響的全面回顧 |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | 綜述 | Wien Med Wochenschr | 慢性 B 型及 C 型肝炎的目前治療策略與未來展望，兩類病毒的機轉差異使治療藥物無法通用 |

> 所有文獻均為間接證據，聚焦 HBV/HCV 共感染管理或治療策略對比，無任何文獻直接研究 Entecavir 作為 HCV 治療藥物的療效。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
Entecavir 靶向 HBV DNA 聚合酶（逆轉錄酶），與 HCV 複製所依賴的 NS5B RNA 依賴性 RNA 聚合酶在結構與功能上完全不同，體外實驗未見直接抗 HCV 活性，機轉聯結缺失。更關鍵的是，目前 DAA 療法（Sofosbuvir/Ledipasvir 等）對 HCV 已達 >95% 持續病毒學應答（SVR），即使 Entecavir 存在微弱的 HCV 活性，亦無實質臨床再利用價值。

**若要推進需要：**
- 確認 Entecavir 三磷酸鹽對 HCV 複製系統（replicon assay）的 IC₅₀，排除體外活性可能性
- 補充完整作用機轉資料（MOA），尤其是核苷類似物跨病毒酶抑制的選擇性分析
- 若資源有限，建議優先評估 **Rank 9（HEV 感染，Research Question 決策）**，其機轉連結相對合理（HEV 為 +ssRNA 病毒，體外數據初步提示 IC₅₀ 約 0.5–5 µM），且現有替代治療（Ribavirin 禁忌症患者）存在未被滿足的臨床需求
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

