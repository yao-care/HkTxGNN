---
layout: default
title: Omeprazole
parent: 僅模型預測 (L5)
nav_order: 545
evidence_level: L5
indication_count: 2
---

# Omeprazole
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

# Omeprazole：從胃酸相關疾病到十二指腸胃逆流

## 一句話總結

Omeprazole 是質子幫浦抑制劑（PPI），原本用於消化性潰瘍、逆流性食道炎等胃酸相關疾病。
TxGNN 模型預測它可能對**十二指腸胃逆流 (Duodenogastric Reflux)** 有效，
目前有 **1 個臨床試驗**和 **20 篇文獻**支持這個方向，但多屬機轉／觀察性研究，尚無直接針對此適應症的隨機對照試驗。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 胃酸相關疾病（消化性潰瘍、逆流性食道炎等）——香港許可證資料缺失，無法列出正式核准適應症文字 |
| 預測新適應症 | 十二指腸胃逆流 (Duodenogastric Reflux) |
| TxGNN 預測分數 | 99.64%（score 0.99642，排名第 7131） |
| 證據等級 | L3（人體觀察性研究，無專門針對此適應症的完成 RCT） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Evidence Pack 中未提供 Omeprazole 的作用機轉資料（[Data Gap]）。就已知藥理學背景，Omeprazole 屬質子幫浦抑制劑（PPI），透過不可逆抑制胃壁細胞 H⁺/K⁺-ATPase 來降低胃酸分泌，此為 PPI 類藥物的共通機轉。

十二指腸胃逆流 (DGR) 的病理機轉牽涉膽汁與十二指腸內容物逆流入胃／食道，胃酸環境的改變會影響逆流物對黏膜的刺激程度。文獻中多篇研究直接探討 Omeprazole 對 DGR 的影響（如降低或改變逆流物性質），顯示兩者機轉上具有直接關聯性；但也有研究提出胃酸抑制可能改變逆流物的細胞毒性、甚至在動物模型中觀察到促進黏膜增生的訊號，顯示此關聯性方向並非單純「治療性」，需要更嚴謹評估。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02685150](https://clinicaltrials.gov/study/NCT02685150) | NA | 已完成 | 157 | 內視鏡三模式影像（NBI/AFI/WLI）用於區分功能性消化不良與逆流性疾病（含酸逆流與膽汁逆流），非直接測試 Omeprazole 療效 |

僅有 1 個相關試驗，且非直接評估 Omeprazole 治療 DGR 的療效試驗，屬於診斷工具研究。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | Eur J Clin Pharmacol | PPI 藥理學與臨床應用回顧，涵蓋消化性潰瘍、GERD 等適應症 |
| [9824338](https://pubmed.ncbi.nlm.nih.gov/9824338/) | 1998 | 臨床研究 | Gut | Omeprazole 20mg 每日兩次可降低 Barrett's 食道患者的十二指腸胃逆流與十二指腸胃食道逆流 |
| [10994616](https://pubmed.ncbi.nlm.nih.gov/10994616/) | 2000 | 臨床研究 | Scand J Gastroenterol | Omeprazole 對 Barrett's 食道患者胃竇十二指腸胃逆流的影響 |
| [16641575](https://pubmed.ncbi.nlm.nih.gov/16641575/) | 2006 | 前瞻性臨床研究（兒童） | J Pediatr Gastroenterol Nutr | Omeprazole 治療兒童食道膽汁逆流的前瞻性研究結果 |
| [19491829](https://pubmed.ncbi.nlm.nih.gov/19491829/) | 2009 | 觀察性研究 | Am J Gastroenterol | 比較 PPI 治療反應者與非反應者的十二指腸胃食道逆流程度 |
| [11232672](https://pubmed.ncbi.nlm.nih.gov/11232672/) | 2001 | 觀察性研究 | Am J Gastroenterol | Barrett's 食道患者的酸/膽汁逆流程度較逆流性食道炎高，PPI 治療效果分析 |
| [21916229](https://pubmed.ncbi.nlm.nih.gov/21916229/) | 2011 | 觀察性研究 | Eksp Klin Gastroenterol | 十二指腸潰瘍患者 DGR 特徵及幽門螺旋桿菌根除後的變化 |
| [12836018](https://pubmed.ncbi.nlm.nih.gov/12836018/) | 2003 | 病例系列 | Eur J Pediatr | 6 名兒童/青少年原發性十二指腸胃逆流病例報告 |
| [33027361](https://pubmed.ncbi.nlm.nih.gov/33027361/) | 2020 | 動物研究 | Acta Cir Bras | Omeprazole 對大鼠 DGR 誘發胃腺癌模型的影響，探討是否具保護作用 |
| [10389684](https://pubmed.ncbi.nlm.nih.gov/10389684/) | 1999 | 動物研究 | Dig Dis Sci | 胃酸阻斷（Omeprazole）在大鼠 DGR 模型中可能促進胃癌發生 — 重要安全訊號 |

> 注意：後兩篇動物研究提示長期胃酸抑制合併 DGR 可能有促進黏膜增生/癌變的訊號，屬於需在安全性評估中特別留意的機轉性警示。

---

## 香港上市資訊

Omeprazole 目前**未於香港取得藥品許可證**（`total_licenses = 0`），Evidence Pack 中無許可證資料可供列表。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 補充說明：本 Evidence Pack 標記 TFDA 仿單警語/禁忌為 **Blocking 等級資料缺口**（DG001），代表目前無法完成安全性初評（S1）；作用機轉（MOA）資料亦缺失（DG002，High 等級）。這兩項資料需優先補齊。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 現有證據多為機轉性／動物研究與觀察性人體研究（L3），尚無專門針對「Omeprazole 治療十二指腸胃逆流」設計的完成 RCT。
- 該藥於香港未上市（0 張許可證），且安全性資料存在 Blocking 等級缺口，無法完成安全性初評。
- 部分動物研究顯示長期胃酸抑制併 DGR 可能有促進癌變的機轉性疑慮，需先釐清風險方向。

**若要推進需要：**
- 取得 TFDA／原廠仿單完整警語與禁忌症資料（解除 DG001 Blocking 缺口）
- 補充 Omeprazole 詳細作用機轉資料（DG002）
- 尋找或發起針對 DGR 適應症的前瞻性臨床研究，釐清療效與致癌訊號的關聯性
- 評估香港上市可行性（目前無許可證登記）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

