---
layout: default
title: Terbutaline
parent: 高證據等級 (L1-L2)
nav_order: 848
evidence_level: L1
indication_count: 3
---

# Terbutaline
{: .fs-9 }

證據等級: **L1** | 預測適應症: **3** 個
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

# Terbutaline：從原適應症（資料未載明）到阻塞性肺病 (Obstructive Lung Disease)

## 一句話總結

Terbutaline 是選擇性 β2 腎上腺素受體促效劑，輸入資料未載明其原適應症。
TxGNN 模型預測它可能對**阻塞性肺病 (Obstructive Lung Disease)** 有效，
目前有 **47 個臨床試驗**（其中多個已完成的 Phase 3）和 **20 篇文獻**支持這個方向。
不過這很可能是既有（核准或近核准）用途，不是真正的新用途。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 阻塞性肺病 (Obstructive Lung Disease) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 19 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Terbutaline 是選擇性 β2 腎上腺素受體促效劑。它經由 cAMP 路徑使呼吸道平滑肌鬆弛，產生支氣管擴張作用，用於可逆性氣道阻塞（氣喘、COPD）。

阻塞性肺病的核心問題是氣道痙攣與氣流受限，這正是 β2 促效劑的作用標的，因此機轉上的關聯直接且已有藥理學基礎。氣喘與 COPD 的臨床試驗和文獻中，terbutaline 都常被當作支氣管擴張劑或急救用藥（reliever）。

目前缺乏 DrugBank 的詳細作用機轉資料，也沒有原適應症紀錄。因此無法確認這個適應症是否為真正的「老藥新用」，較可能是已確立的用途。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06626620](https://clinicaltrials.gov/study/NCT06626620) | Phase 3 | 完成 | 120 | 兒童氣喘急性發作：靜脈注射硫酸鎂 vs terbutaline，terbutaline 為直接比較組（直接證據） |
| [NCT02224157](https://clinicaltrials.gov/study/NCT02224157) | Phase 3 | 完成 | 4215 | Symbicort 視需要使用 vs Pulmicort 每日兩次加 terbutaline 視需要使用，terbutaline 為對照組急救藥 |
| [NCT02149199](https://clinicaltrials.gov/study/NCT02149199) | Phase 3 | 完成 | 3850 | Symbicort 視需要使用 vs terbutaline 視需要使用 vs Pulmicort 加 terbutaline，用於氣喘 |
| [NCT00839800](https://clinicaltrials.gov/study/NCT00839800) | Phase 3 | 完成 | 2091 | Symbicort SMART vs Symbicort 加 terbutaline 視需要使用，為期 12 個月，terbutaline 為對照組急救藥 |
| [NCT00252863](https://clinicaltrials.gov/study/NCT00252863) | Phase 3 | 完成 | 1600 | Symbicort 單一吸入器療法 vs 常規最佳療法，用於成人持續性氣喘 |
| [NCT00849095](https://clinicaltrials.gov/study/NCT00849095) | Phase 3 | 完成 | 860 | 視需要使用 budesonide/formoterol vs 規律使用 budesonide/formoterol 加視需要使用 terbutaline，用於輕中度氣喘 |
| [NCT00326053](https://clinicaltrials.gov/study/NCT00326053) | Phase 3 | 完成 | 600 | Symbicort vs Pulmicort 加 terbutaline 視需要使用，預防急診出院後氣喘復發 |
| [NCT02322788](https://clinicaltrials.gov/study/NCT02322788) | Phase 3 | 完成 | 95 | Bricanyl Turbuhaler M3 vs M2，以乙醯甲膽鹼誘發支氣管收縮評估保護效果 |
| [NCT01096017](https://clinicaltrials.gov/study/NCT01096017) | Phase 3 | 完成 | 24 | 日本成人氣喘：terbutaline Turbuhaler 0.4 mg vs salbutamol pMDI 200 μg 的相對療效（單劑量、交叉設計） |
| [NCT00750568](https://clinicaltrials.gov/study/NCT00750568) | N/A | 未知 | 36 | 重度氣喘持續狀態兒童：terbutaline 連續靜脈輸注的藥動學與藥效學 |

說明：多數試驗中 terbutaline 是對照組的急救藥，屬間接證據。直接以 terbutaline 為受試藥物的大型試驗不多。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [3073804](https://pubmed.ncbi.nlm.nih.gov/3073804/) | 1988 | RCT | Br J Dis Chest | 口服 terbutaline 使 COPD 患者最大吸氣口腔壓平均增加 5.8 cmH2O，橫膈壓增加 5.0 cmH2O |
| [30156361](https://pubmed.ncbi.nlm.nih.gov/30156361/) | 2019 | RCT | Acad Emerg Med | 雙盲試驗，比較霧化 terbutaline 加 ipratropium 與單用 terbutaline，對象為需無創通氣的 COPD 急性發作患者 |
| [6988343](https://pubmed.ncbi.nlm.nih.gov/6988343/) | 1980 | RCT | Int J Clin Pharmacol Ther Toxicol | 雙盲兩週試驗，比較口服 clenbuterol 與 terbutaline 對阻塞性肺病的支氣管擴張效果 |
| [10384064](https://pubmed.ncbi.nlm.nih.gov/10384064/) | 1999 | RCT | Lung | 雙盲、安慰劑對照、交叉試驗（26 人），評估單劑 terbutaline 對 COPD 肺功能與運動能力的影響 |
| [36227333](https://pubmed.ncbi.nlm.nih.gov/36227333/) | 2023 | 系統性回顧 | Naunyn Schmiedebergs Arch Pharmacol | 回顧 terbutaline 在人體的藥動學，涵蓋給藥途徑、年齡、疾病狀態、吸菸等因素的影響 |
| [33065789](https://pubmed.ncbi.nlm.nih.gov/33065789/) | 2020 | 臨床研究 | Ann Palliat Med | 探討 N-乙醯半胱胺酸合併 terbutaline 用於老年 COPD 的臨床價值及對細胞凋亡機制的影響 |
| [336304](https://pubmed.ncbi.nlm.nih.gov/336304/) | 1977 | 臨床研究 | Chest | 比較 atropine 與 terbutaline 在 39 名慢性支氣管炎與 16 名穩定氣喘患者的支氣管擴張反應 |
| [18761816](https://pubmed.ncbi.nlm.nih.gov/18761816/) | 2008 | 臨床研究 | Cell Mol Immunol | 霧化吸入 terbutaline 與 budesonide 可改善 AECOPD 患者的免疫功能與肺功能 |
| [6624778](https://pubmed.ncbi.nlm.nih.gov/6624778/) | 1983 | 臨床研究 | Am J Med | 雙盲交叉試驗（17 人），比較口服 aminophylline、terbutaline 與吸入 albuterol，吸入 albuterol 的 FEV1 改善較明顯 |
| [8882073](https://pubmed.ncbi.nlm.nih.gov/8882073/) | 1996 | 臨床研究 | Thorax | 探討 COPD 患者停用 terbutaline 後是否出現氣道反應性反彈與支氣管收縮反彈 |

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-48007 | TERBUTA TAB 2.5MG | CHRISTO PHARM LTD |
| HK-46514 | BALTIC-D TAB 2.5MG | NATURAL HEALTH RESOURCES COMPANY LIMITED |
| HK-49032 | VICKTALINE SYRUP 3MG/5ML | VICKMANS LABORATORIES LTD |
| HK-48008 | TERBUTA SYRUP 1.5MG/5ML | CHRISTO PHARM LTD |
| HK-55764 | APT-TERBUTALINE SR TAB 5MG | APT PHARMA LIMITED |

說明：以上為 19 張許可證中的 5 張，劑型從品名判讀（錠劑、糖漿、緩釋錠）。許可證資料未收錄核准適應症文字。

## 安全性考量

安全性資訊請參考原廠仿單。

預測評估中建議的防護重點如下：
- 需監測心搏過速、低血鉀與震顫。
- 心血管疾病患者需謹慎使用。
- 解讀結果時，需對照具體適應症、族群與劑型。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有多個已完成的 Phase 3 試驗（含 1 個以 terbutaline 為直接比較組的 RCT）和多篇 RCT 文獻，證據等級達 L1。但多數試驗中 terbutaline 只是對照組急救藥，且這很可能是既有用途，不是真正的新適應症。
- 香港仿單的警語與禁忌資料缺口屬阻擋性（Blocking），需補齊才能進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊警語與禁忌症。
- 補齊 DrugBank 的作用機轉與原適應症，確認這個適應症是否已在核准範圍內。
- 針對特定劑型與族群（兒童、孕婦、心血管疾病患者）訂定安全性監測計畫。

**其他預測適應症：**
- 呼吸道畸形（證據等級 L4，建議 Hold）：證據僅有個案報告與氣喘相關研究，且文獻中有 terbutaline 暴露與神經發展的安全疑慮，兒童與孕婦使用需審慎評估。
- Rienhoff 症候群（證據等級 L5，建議 Hold）：僅有模型預測，無試驗或文獻，也無機轉依據。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

