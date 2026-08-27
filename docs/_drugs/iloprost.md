---
layout: default
title: Iloprost
parent: 僅模型預測 (L5)
nav_order: 389
evidence_level: L5
indication_count: 5
---

# Iloprost
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

# Iloprost：從肺動脈高壓到先天性心臟病相關肺動脈高壓

## 一句話總結

Iloprost 是吸入型前列環素（prostacyclin）類似物，文獻顯示其已核准用於成人肺動脈高壓（PAH）之治療。
TxGNN 模型與相關文獻證據共同指向它可能適用於更細分的族群——**先天性心臟病相關肺動脈高壓（PAH associated with congenital heart disease，含 Eisenmenger 症候群、小兒族群）**，
目前有 **1 個臨床試驗**和 **20 篇文獻**支持這個方向（本報告呈現其中最相關的 10 篇）。

> **說明**：TxGNN 對此藥物共產生 5 個高分預測，其中數值最高的兩項（稀毛症相關疾病）完全沒有臨床試驗或文獻佐證，且系統自身的機轉分析已指出這很可能是知識圖譜中「前列腺素類藥物」嵌入相似性造成的偽陽性，而非真實藥理關聯。因此本報告以證據等級最高、唯一達到 L3 等級的候選適應症（先天性心臟病相關 PAH）作為評估主軸，其餘候選整理於文末〈其他 TxGNN 預測〉供參考。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未提供本地許可證來源（香港未上市）；依文獻（PMID 24729548）iloprost 已核准用於成人肺動脈高壓 |
| 預測新適應症 | 先天性心臟病相關肺動脈高壓 (Pulmonary Arterial Hypertension Associated with Congenital Heart Disease) |
| TxGNN 預測分數 | 99.32% |
| 證據等級 | L3（有觀察性/世代研究支持，尚無已完成之 Phase 2/3 RCT） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Iloprost 是吸入性前列環素（PGI2）類似物，透過活化 IP 受體、啟動 cAMP 訊息路徑，產生肺血管平滑肌舒張、抑制血小板聚集、並抑制血管重塑作用。這是 WHO Group 1 肺動脈高壓（PAH）已建立的病理生理標靶治療機轉，與現行國際 PAH 治療指引一致。

先天性心臟病相關 PAH（含 Eisenmenger 症候群）屬於 WHO Group 1 PAH 的一個臨床亞型，其肺血管阻力增加、內皮功能失調的病理機轉與原發性 PAH 相同，因此已核准用於一般成人 PAH 的 iloprost，在機轉上延伸適用於此亞型具有合理性。文獻也顯示，iloprost 目前已被實際使用於小兒與 CHD 相關 PAH 族群（如急性血液動力學測試、長期吸入治療），顯示此為藥物既有適應症的族群擴展，而非全新的機轉假設。

需注意的是，此候選適應症目前仍缺乏已完成的大型隨機對照試驗（現有臨床試驗為 Phase 標記 N/A、狀態未知），現有證據以世代研究、回溯性分析與案例系列為主，因此證據強度僅達 L3，尚不足以直接支持常規臨床決策。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01383083](https://clinicaltrials.gov/study/NCT01383083) | N/A | 未知 (Unknown) | 42 | 評估 Iloprost 於成人先天性心臟病相關 PAH（Eisenmenger 生理）之安全性、耐受性、臨床及血液動力學效果 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [19436672](https://pubmed.ncbi.nlm.nih.gov/19436672/) | 2009 | Review | Vascular Health and Risk Management | 回顧吸入性 iloprost 用於控制小兒肺動脈高壓（含 CHD 相關族群）之證據 |
| [18260882](https://pubmed.ncbi.nlm.nih.gov/18260882/) | 2007 | Review | Kardiologiia | 回顧前列環素類似物於原發性/次發性 PAH（含 CHD 相關）對照試驗結果 |
| [28608969](https://pubmed.ncbi.nlm.nih.gov/28608969/) | 2017 | Cohort | Clin Exp Pharmacol Physiol | Iloprost 可調節 CHD-PAH 患者 NO、ET-1、ADMA 等內皮功能生物標記 |
| [29426959](https://pubmed.ncbi.nlm.nih.gov/29426959/) | 2018 | Cohort | Pediatric Cardiology | 吸入性 iloprost 對單純 CHD 相關 PAH 兒童具急性血液動力學改善且安全性良好 |
| [27053694](https://pubmed.ncbi.nlm.nih.gov/27053694/) | 2016 | Cohort（歐洲共識） | Heart | 歐洲小兒肺高壓共識：血液動力學評估與急性血管反應測試方法學（含 iloprost 使用情境） |
| [24729548](https://pubmed.ncbi.nlm.nih.gov/24729548/) | 2015 | 回溯性世代研究 | Pediatric Pulmonology | 長期使用吸入性 iloprost 治療兒童 PH，顯示臨床改善，並指出 iloprost 已核准用於成人 PH |
| [36010107](https://pubmed.ncbi.nlm.nih.gov/36010107/) | 2022 | Case Series | Children (Basel) | Eisenmenger 症候群患者以 sildenafil + bosentan + iloprost 合併治療之長期案例系列 |
| [30719004](https://pubmed.ncbi.nlm.nih.gov/30719004/) | 2018 | 前瞻性研究 | Frontiers in Pharmacology | 急性吸入 iloprost 可改善 PAH 患者右心室功能（心臟磁振造影證實） |
| [25316472](https://pubmed.ncbi.nlm.nih.gov/25316472/) | 2014 | Case Report | Saudi Medical Journal | 未修補 VSD 合併重度 PAH 患者，密集吸入性 iloprost 療程使心包積液完全消退 |
| [22621693](https://pubmed.ncbi.nlm.nih.gov/22621693/) | 2012 | Review | Drugs | 結締組織病相關 PAH（CTD-APAH）治療回顧，涵蓋前列環素類藥物角色 |

---

## 其他 TxGNN 預測（僅供參考，證據不足）

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 決策 | 備註 |
|------|-----------|-----------|---------|------|------|
| 1 | Hypotrichosis simplex of the scalp | 99.45% | L5 | Hold | 無任何臨床試驗/文獻；系統判斷可能為前列腺素類藥物嵌入相似性造成的偽陽性，藥理類比薄弱 |
| 2 | Congenital hypotrichosis milia | 99.33% | L5 | Hold | 同上，屬遺傳性外胚層發育疾病，與 iloprost 機轉無已知關聯 |
| 4 | Pulmonary arteriovenous malformation | 99.31% | L4 | Hold | 結構性血管分流疾病，與 PAH 病理機轉不同，缺乏直接治療理論基礎 |
| 5 | PAH associated with chronic hemolytic anemia | 99.21% | L4 | Research Question | 機轉上有理論重疊，但此亞型血液動力學特性特殊且完全無直接證據，值得列為研究問題 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 本評估目前存在一項**阻斷性資料缺口（Blocking Data Gap）**：尚未取得藥品仿單警語與禁忌症資料，因此無法完成 S1 安全性初評，這是推進此候選適應症前必須優先補齊的項目。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 先天性心臟病相關 PAH 屬於 iloprost 既有 PAH 適應症的臨床亞型延伸，機轉合理且有多篇世代研究/案例系列（含小兒族群、Eisenmenger 症候群）支持其實際使用經驗，證據等級達 L3。
- 然而現有臨床試驗僅 1 項且階段/狀態不明，尚無已完成的 Phase 2/3 RCT，加上仿單警語與禁忌症資料完全缺失（Blocking Data Gap），不足以直接支持常規推廣，須在明確防護措施下謹慎推進。

**若要推進需要：**
- 取得藥品仿單警語與禁忌症資料（解除 DG001 阻斷項，完成 S1 安全性初評）
- 補充作用機轉（MOA）之正式藥理資料（DG002），強化機轉關聯性分析
- 評估是否有進行中或規劃中的 Phase 2/3 RCT，特別針對小兒與 Eisenmenger 症候群族群
- 釐清香港上市狀態與潛在的許可證申請路徑（目前為未上市、0 張許可證）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

