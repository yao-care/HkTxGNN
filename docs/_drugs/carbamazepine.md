---
layout: default
title: Carbamazepine
parent: 中證據等級 (L3-L4)
nav_order: 136
evidence_level: L3
indication_count: 10
---

# Carbamazepine
{: .fs-9 }

證據等級: **L3** | 預測適應症: **10** 個
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

# Carbamazepine：從癲癇／三叉神經痛到三叉神經腫瘤

## 一句話總結

Carbamazepine 是廣泛使用的第一線抗癲癇與神經痛藥物，全球已核准用於癲癇發作及三叉神經痛治療。TxGNN 模型預測它可能對**三叉神經腫瘤 (Trigeminal Nerve Neoplasm)** 有效，目前有 **1 個臨床試驗**和 **20 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無香港核准紀錄（全球已核准用於癲癇、三叉神經痛） |
| 預測新適應症 | 三叉神經腫瘤 (Trigeminal Nerve Neoplasm) |
| TxGNN 預測分數 | 99.998% |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Carbamazepine 是電壓依賴性鈉通道阻斷劑（voltage-gated sodium channel blocker），透過穩定神經元膜電位、抑制高頻重複放電，達到抗癲癇與鎮痛效果。雖然本 Evidence Pack 的 MOA 欄位標記為資料缺口，但 CBZ 鈉通道阻斷的藥理機轉已在神經藥理學文獻中廣泛驗證。

三叉神經腫瘤（包括神經鞘瘤、脂肪瘤、惡性淋巴瘤等）可透過壓迫或浸潤三叉神經纖維，引發異位放電（ectopic discharge），臨床上表現為三叉神經痛（TN）或反射性癲癇發作。CBZ 鈉通道阻斷機轉理論上可抑制此類異位放電，緩解腫瘤壓迫性神經痛症狀。TxGNN 模型正是透過「TN ↔ 腫瘤性壓迫」的疾病本體論連結捕捉到此預測訊號。

需特別注意的是：現有案例報告顯示，當三叉神經痛症狀對 CBZ **無反應**時，反而提示臨床醫師應進一步影像學排查腫瘤病因。因此 CBZ 在本適應症的潛在角色，主要是**症狀緩解（symptom management）**，而非直接的抗腫瘤治療。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06853119](https://clinicaltrials.gov/study/NCT06853119) | N/A | 尚未招募 | 120 | MRI 分析三叉神經痛患者的腦網絡動態變化與微結構，評估血腦屏障及水交換率，探索神經可塑性機轉（純觀察性影像研究，不測試 CBZ 療效） |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36824641](https://pubmed.ncbi.nlm.nih.gov/36824641/) | 2022 | Review | Acta Clinica Croatica | CBZ 為三叉神經痛第一線醫療用藥；腫瘤性壓迫為繼發性 TN 的病因之一 |
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Review of Neurotherapeutics | TN 多種治療方式系統回顧；CBZ 仍是主要藥物選擇；血管壓迫引起局部脫髓鞘和異位放電的機轉 |
| [30741017](https://pubmed.ncbi.nlm.nih.gov/30741017/) | 2023 | Case Report | British Journal of Neurosurgery | 三叉神經原發性惡性淋巴瘤；CBZ 處方後症狀未改善，MRI 確認 Meckel's cave 腫塊——呈現 CBZ 無效即應排查腫瘤的典型路徑 |
| [25142539](https://pubmed.ncbi.nlm.nih.gov/25142539/) | 2014 | Case Report | 臨床神経学 | 惡性淋巴瘤沿三叉神經蔓延；初始 CBZ 治療有效，四個月後出現非神經痛性鈍痛及複視等顱神經症狀 |
| [15235745](https://pubmed.ncbi.nlm.nih.gov/15235745/) | 2004 | Case Report | Arquivos de Neuro-Psiquiatria | Meckel's cave 原發性黑色素瘤；TN 疼痛對 CBZ 無效，微血管減壓術後復發，最終確診腫瘤 |
| [25968963](https://pubmed.ncbi.nlm.nih.gov/25968963/) | 2015 | Case Report/Review | World Neurosurgery | 靜脈血管瘤引發 TN；CBZ 為標準初始治療；中央髓鞘機械性損傷與異常傳導的機轉 |
| [3181365](https://pubmed.ncbi.nlm.nih.gov/3181365/) | 1988 | 動物研究 | Experimental Neurology | CBZ 靜脈給藥立即抑制實驗性神經瘤的自發放電（A-α/β 及 A-δ 纖維），提供 CBZ 對神經瘤異位放電的直接藥理學證據 |
| [25433061](https://pubmed.ncbi.nlm.nih.gov/25433061/) | 2014 | Case Report/Review | Neurological Surgery | 腦橋小腦角脂肪瘤引發 TN；CBZ 因副作用控制不佳而接受手術切除部分腫瘤 |
| [22647513](https://pubmed.ncbi.nlm.nih.gov/22647513/) | 2012 | Case Report | Neurological Surgery | 合併舌咽神經痛與三叉神經痛；CBZ 為功能性顱神經痛的第一線藥物，失效則轉微血管減壓術 |
| [33989821](https://pubmed.ncbi.nlm.nih.gov/33989821/) | 2021 | Case Report | World Neurosurgery | 岩斜區腦膜瘤引發 TN；腫瘤包裹第五對顱神經，以 Kawase 入路切除；CBZ 為術前症狀控制藥物 |

---

## 香港上市資訊

目前無香港上市許可證紀錄（total_licenses = 0）。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
現有文獻的核心訊號是「三叉神經腫瘤引發 TN 症狀，CBZ 用於症狀緩解」，而非 CBZ 直接治療或改變三叉神經腫瘤本身的自然病程。多份案例報告顯示 CBZ 對腫瘤性 TN 的療效不一（部分有效、部分無效），且 CBZ 治療失敗往往反而是發現腫瘤的重要臨床線索。CBZ 在香港目前無上市核准，安全性資料欠缺，尚無法進入正式評估。

**若要推進需要：**
- 釐清研究定位：確認以「腫瘤性 TN 的症狀緩解」而非「抗腫瘤」作為老藥新用方向，後者缺乏機轉支持
- 補充完整 MOA 資料（DrugBank API 查詢 DB00564）
- 取得仿單警語與禁忌症（TFDA 官網下載 PDF 解析，DG001 缺口）
- 設計針對三叉神經腫瘤壓迫性疼痛症狀控制的前瞻性觀察性研究或病例系列分析
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

