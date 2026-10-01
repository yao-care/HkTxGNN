---
layout: default
title: Magnesium Sulfate
parent: 高證據等級 (L1-L2)
nav_order: 541
evidence_level: L1
indication_count: 5
---

# Magnesium Sulfate
{: .fs-9 }

證據等級: **L1** | 預測適應症: **5** 個
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

# 硫酸鎂 (Magnesium Sulfate)：從許可證未載明的原適應症到子癇前症／子癇

## 一句話總結

硫酸鎂在香港已有 11 張許可證，但許可證資料未載明核准適應症。
TxGNN 模型預測它可能對**子癇前症／子癇 (Preeclampsia/Eclampsia)** 有效，目前有 **48 個臨床試驗**和 **20 篇文獻**支持這個方向。
不過這項預測本身已是國際標準治療，較接近資料補全，而不是真正的新用途。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明 |
| 預測新適應症 | 子癇前症／子癇 (Preeclampsia/Eclampsia) |
| TxGNN 預測分數 | 99.999% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 11 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，硫酸鎂是子癇預防與治療的既定抗痙攣藥物。文獻提出的可能機轉包括 NMDA 受體拮抗、鈣離子通道阻斷與腦血管擴張。

子癇前症的嚴重併發症是子癇抽搐。一般認為腦血管痙攣與腦灌流異常參與其病理，而鎂可能透過對抗鈣依賴的血管收縮來減輕血管痙攣。因此在機轉上，這個預測合理。

但要提醒的是，這個適應症已是標準治療。由於原適應症和 MOA 欄位皆為空，這筆預測比較像資料完整性問題，而不是真正的老藥新用候選。

## 臨床試驗證據

以下依相關性與研究設計挑選 10 個（共 48 筆）。資料僅含試驗設計摘要，未包含結果數據。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01846156](https://clinicaltrials.gov/study/NCT01846156) | Phase 3 | 完成 | 240 | 比較嚴重子癇前症的不同硫酸鎂給藥方案 |
| [NCT02307201](https://clinicaltrials.gov/study/NCT02307201) | Phase 2/3 | 完成 | 1114 | 術前已用藥 8 小時以上者，產後用 24 小時 vs 不繼續使用 |
| [NCT02317146](https://clinicaltrials.gov/study/NCT02317146) | Phase 2/3 | 完成 | 280 | 產前用藥不足 8 小時者，產後 6 小時 vs 24 小時 |
| [NCT03164304](https://clinicaltrials.gov/study/NCT03164304) | Phase 4 | 完成 | 222 | 嚴重子癇前症維持劑量 1 g vs 2 g 的療效與安全性 |
| [NCT01408979](https://clinicaltrials.gov/study/NCT01408979) | Phase 4 | 完成 | 120 | 嚴重子癇前症產後短療程預防 |
| [NCT03318211](https://clinicaltrials.gov/study/NCT03318211) | Phase 4 | 未知 | 100 | 產後持續 vs 停止硫酸鎂 |
| [NCT02835339](https://clinicaltrials.gov/study/NCT02835339) | Phase 4 | 完成 | 66 | 肥胖子癇前症婦女的硫酸鎂藥物代謝與給藥 |
| [NCT04645719](https://clinicaltrials.gov/study/NCT04645719) | Phase 3 | 未知 | 75 | 肥胖患者的最佳硫酸鎂輸注劑量 |
| [NCT00004399](https://clinicaltrials.gov/study/NCT00004399) | 未標示 | 完成 | 2000 | Nimodipine 對比硫酸鎂預防子癇抽搐 |
| [NCT07220902](https://clinicaltrials.gov/study/NCT07220902) | Phase 3 | 尚未招募 | 1240 | Levetiracetam 對比硫酸鎂預防子癇抽搐（等效性試驗） |

## 文獻證據

其中 Magpie 試驗與 Cochrane 回顧來自同義項目「toxemia of pregnancy」，兩者證據基礎相同。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [12057549](https://pubmed.ncbi.nlm.nih.gov/12057549/) | 2002 | RCT | Lancet | Magpie 試驗：硫酸鎂對比安慰劑用於子癇前症 |
| [12576241](https://pubmed.ncbi.nlm.nih.gov/12576241/) | 2003 | RCT | Obstet Gynecol | 硫酸鎂對輕度子癇前症疾病進展的影響 |
| [38865319](https://pubmed.ncbi.nlm.nih.gov/38865319/) | 2024 | RCT | PLoS One | Springfusor 幫浦對比標準肌肉注射的接受度 |
| [21069663](https://pubmed.ncbi.nlm.nih.gov/21069663/) | 2010 | 系統性回顧 | Cochrane Database Syst Rev | 硫酸鎂與其他抗痙攣藥用於預防子癇 |
| [34187284](https://pubmed.ncbi.nlm.nih.gov/34187284/) | 2022 | 系統性回顧／統合分析 | J Matern Fetal Neonatal Med | 產後硫酸鎂療程長短對子癇的影響 |
| [39054515](https://pubmed.ncbi.nlm.nih.gov/39054515/) | 2024 | 系統性回顧／統合分析 | BMC Womens Health | 12 小時與 24 小時硫酸鎂的療效與安全性比較 |
| [9794688](https://pubmed.ncbi.nlm.nih.gov/9794688/) | 1998 | Review | Obstet Gynecol | 硫酸鎂預防抽搐的療效、益處與風險 |
| [2288560](https://pubmed.ncbi.nlm.nih.gov/2288560/) | 1990 | Review | Am J Obstet Gynecol | 主張硫酸鎂為子癇前症的理想抗痙攣藥 |
| [16978425](https://pubmed.ncbi.nlm.nih.gov/16978425/) | 2006 | Review | Obstet Gynecol Surv | 子癇前症腦血流動力學與替代硫酸鎂的理由 |
| [36413336](https://pubmed.ncbi.nlm.nih.gov/36413336/) | 2023 | 未分類 | Biol Trace Elem Res | 重度子癇前症用藥後嚴重高鎂血症的發生率與風險因子 |

## 香港上市資訊

共 11 張許可證，以下列出 5 張。各證載明的劑型與核准適應症在資料中皆為空白。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-32142 | MAGNESIUM SULPHATE CONCENTRATED INJ 49.3%（輝瑞） | 未載明（品名為注射液） | 未載明 |
| HK-47730 | CHESTOK ENEMA（Europharm） | 未載明（品名為灌腸劑） | 未載明 |
| HK-47731 | PERSTON ENEMA（Europharm） | 未載明（品名為灌腸劑） | 未載明 |
| HK-52179 | QUICK MICROENEMA ENEMA（Europharm） | 未載明（品名為灌腸劑） | 未載明 |
| HK-47729 | HARRICO ENEMA（Europharm） | 未載明（品名為灌腸劑） | 未載明 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有多個已完成的 Phase 2/3 與 Phase 3 試驗，另有 Magpie RCT 與 Cochrane 回顧支持，證據等級為 L1。
- 這是既有的標準治療，而非全新適應症。香港的核准適應症與仿單資料仍缺，安全性篩選無法進行。

**若要推進需要：**
- 取得香港衞生署仿單，確認核准適應症、警語與禁忌症（此為阻斷性缺口）。
- 補充作用機轉資料（DrugBank）。
- 建立用藥防護：
  - 監測血清鎂濃度與中毒徵象（反射、呼吸速率、尿量）。
  - 依腎功能與肥胖調整劑量。
  - 備妥葡萄糖酸鈣作為解毒劑。
  - 產後用藥時間依 12 小時與 24 小時相關試驗結果決定。

**同一藥物的其他預測（不建議推進）：**
- **toxemia of pregnancy**：與子癇前症重複，建議整併。
- **thrombotic disease**：僅有 1 個 Phase 3 試驗（TTP，MAGMAT），且結果尚待核實，建議 Hold。
- **pharyngitis**：現有證據是術後喉嚨痛而非感染性咽炎，僅能作為研究問題。
- **nasal cavity disease**：僅有模型預測，無有效證據（L5），建議 Hold。

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

