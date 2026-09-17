---
layout: default
title: Ticagrelor
parent: 高證據等級 (L1-L2)
nav_order: 745
evidence_level: L2
indication_count: 5
---

# Ticagrelor
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# Ticagrelor：從急性冠心症到顱內動脈粥狀硬化

## 一句話總結

> Ticagrelor 是一種 P2Y12 受體拮抗劑，屬於既有的抗血小板藥物，核心適應症為急性冠心症及 PCI（經皮冠狀動脈介入）後的血栓事件預防。
> TxGNN 模型預測它可能對**顱內動脈粥狀硬化 (Intracranial Arteriosclerosis)** 有效，
> 目前有 **11 個臨床試驗**和 **3 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 急性冠心症／PCI 後抗血小板治療（既有國際核心適應症；香港尚未上市，無本地許可證資料） |
| 預測新適應症 | 顱內動脈粥狀硬化 (Intracranial Arteriosclerosis) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

DrugBank 正式的作用機轉（MOA）欄位目前為資料缺口（見安全性段落 DG002）。不過根據評估團隊的機轉關聯分析，Ticagrelor 為 **P2Y12 受體拮抗劑**，透過抑制血小板活化與聚集來阻斷動脈血栓形成，這正是顱內動脈粥狀硬化 (ICAD) 引發缺血性中風的核心病理機轉之一。

顱內動脈粥狀硬化與 Ticagrelor 原本核心適應症（冠狀動脈疾病、周邊動脈疾病）同屬「動脈粥狀硬化導致血栓事件」的疾病族群，僅發生血管床不同（顱內 vs. 冠狀動脈/周邊動脈）。目前臨床實務上，雙重抗血小板治療 (DAPT) 已被延伸應用於顱內支架植入與嚴重顱內狹窄病人，CAPTIVA、DREAM-PRIDE 等大型 Phase 3 試驗正是針對此一族群設計。

由於機轉與現有 DAPT 策略高度一致，且已有多個大型隨機對照試驗在此族群中進行，這個預測在機轉層面具合理性，但目前多數關鍵試驗仍在進行中，尚未有最終療效結果。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05047172](https://clinicaltrials.gov/study/NCT05047172) | Phase 3 | 進行中（未招募） | 1683 | CAPTIVA 試驗：比較 rivaroxaban、ticagrelor 及兩者併用是否優於 clopidogrel，降低顱內動脈狹窄病人 1 年內缺血性中風/出血/血管死亡率 |
| [NCT02605447](https://clinicaltrials.gov/study/NCT02605447) | Phase 4 | 已完成 | 2009 | EVOLVE Short DAPT：評估高出血風險病人於 PCI 後 3 個月 DAPT 之安全性 |
| [NCT06714526](https://clinicaltrials.gov/study/NCT06714526) | NA | 招募中 | 100 | 基因型導引 P2Y12 抑制劑選擇 vs. 傳統 clopidogrel，用於症狀性顱內動脈狹窄 |
| [NCT04948749](https://clinicaltrials.gov/study/NCT04948749) | NA | 招募中 | 792 | DREAM-PRIDE：藥物釋放支架 + 積極藥物治療 vs. 標準藥物治療，預防症狀性顱內動脈粥狀硬化復發中風 |
| [NCT01732822](https://clinicaltrials.gov/study/NCT01732822) | Phase 3 | 已完成 | 13885 | Ticagrelor vs. clopidogrel 於周邊動脈疾病及缺血性中風/TIA 病人之心血管死亡、心肌梗塞、缺血性中風風險比較 |
| [NCT06058130](https://clinicaltrials.gov/study/NCT06058130) | NA | 狀態未知 | 2171 | 抗血小板併抗凝血治療用於合併心房顫動與顱內外動脈狹窄之急性缺血性中風病人 |
| [NCT01813435](https://clinicaltrials.gov/study/NCT01813435) | Phase 3 | 已完成 | 15991 | GLOBAL LEADERS：支架植入後兩種抗血小板治療策略比較（一般冠脈族群） |
| [NCT07164859](https://clinicaltrials.gov/study/NCT07164859) | Phase 3 | 尚未招募 | 1700 | 老年 PCI 病人縮短 DAPT 療程接續 P2Y12 抑制劑單一療法之安全性與療效 |
| [NCT03620760](https://clinicaltrials.gov/study/NCT03620760) | Phase 4 | 狀態未知 | 2036 | 低劑量 vs. 標準劑量 Ticagrelor 於不穩定型心絞痛支架術後之療效與安全性 |
| [NCT07354828](https://clinicaltrials.gov/study/NCT07354828) | N/A | 尚未招募 | 3500 | 冠狀動脈血管重建 DAPT 品質控制指標優化與驗證 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39862061](https://pubmed.ncbi.nlm.nih.gov/39862061/) | 2025 | 試驗設計/Review | Int J Stroke | CAPTIVA 試驗設計與早期進展：探討 clopidogrel+aspirin 標準治療後 12 個月內復發中風風險仍高，需其他抗栓組合 |
| [38252758](https://pubmed.ncbi.nlm.nih.gov/38252758/) | 2024 | Review | Stroke | 顱內動脈粥狀硬化研究重點更新，總結現有知識缺口 |
| [39658130](https://pubmed.ncbi.nlm.nih.gov/39658130/) | 2025 | Review | J Neurointerv Surg | 神經介入手術中低劑量 Ticagrelor（60mg bid + aspirin）DAPT 方案之臨床經驗報告 |

---

## 香港上市資訊

Ticagrelor 目前**尚未於香港上市**，無現存許可證或核准適應症紀錄可供比對。

---

## 安全性考量

安全性資訊請參考原廠仿單。（TFDA 仿單警語/禁忌尚未收集，屬 Blocking 資料缺口；藥物交互作用查無資料）

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有兩個 Grade A 等級試驗（CAPTIVA Phase 3 進行中、EVOLVE Short DAPT Phase 4 已完成）直接針對顱內血管粥狀硬化族群評估抗血小板策略，機轉合理性高，但關鍵試驗（CAPTIVA）尚未產出最終療效結果，證據等級為 L2。
- Ticagrelor 目前未在香港上市，推進前需完整的本地法規與安全性資料。

**若要推進需要：**
- 補齊 DrugBank 正式 MOA 資料（DG002，High severity）
- 取得仿單警語與禁忌症資料（DG001，Blocking severity，為進入 S1 安全性初評之必要條件）
- 追蹤 CAPTIVA（NCT05047172）最終結果
- 若考慮在香港申請新適應症，需規劃上市/許可證申請路徑

---

## 其他候選適應症（本次評估之其他預測結果）

本次 Evidence Pack 另包含 4 個預測適應症，供決策參考：

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 決策階段 | 建議 |
|------|-----------|-----------|---------|---------|------|
| 2 | Monckeberg arteriosclerosis | 99.94% | L5 | S0 | Hold（病理機轉為中膜鈣化，非血栓媒介，與抗血小板機轉不符） |
| 3 | Priapism | 99.75% | L4 | S0 | Hold（現有文獻顯示抗栓藥物與性功能障礙為負相關，方向與治療目標相反） |
| 4 | Ischemic disease | 99.64% | L1 | S3 | Proceed with Guardrails（屬既有核心適應症，非嚴格意義再利用，證據極為充分：PLATO、THEMIS、TWILIGHT 等多個 Phase 3 RCT） |
| 5 | May-Thurner syndrome | 99.55% | L5 | S0 | Hold（靜脈血栓疾病，標準治療為抗凝血劑而非抗血小板藥物，無臨床試驗或文獻支持） |

排名 4（ischemic disease）證據最充分，但本質上是 Ticagrelor 既有適應症的再確認，而非新的再利用方向；排名 1（顱內動脈粥狀硬化）是本報告聚焦、真正具「老藥新用」意義且證據品質尚可的候選。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

