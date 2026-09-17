---
layout: default
title: Theophylline
parent: 僅模型預測 (L5)
nav_order: 740
evidence_level: L5
indication_count: 5
---

# Theophylline
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

# Theophylline（茶鹼）：老藥多重再利用機會評估

## 一句話總結

Theophylline（茶鹼）是傳統黃嘌呤類支氣管擴張劑，本評估包（`TW-DB00277-multi`）由 TxGNN 一次產生 **5 個預測適應症**。其中證據最強的是「**阻塞性肺病 (Obstructive Lung Disease)**」（L1，8+ 項含 Phase 3/4 RCT 直接以茶鹼為介入藥物），本質上是確認茶鹼原本已知的臨床用途；其餘 4 項（血栓性疾病、鼻腔疾病、喉氣管炎、氣管疾病）證據等級介於 L2–L5，多屬機轉外推或知識圖譜共現雜訊，尚不足以支持臨床推進。目前作用機轉（MOA）與安全性仿單資料皆為缺口，且香港未上市。

---

## 快速總覽

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 決策階段 | 建議決策 |
|---|---|---|---|---|---|
| 1 | Thrombotic disease（血栓性疾病） | 99.62% | L5 | S0 | Hold |
| 2 | Nasal cavity disease（鼻腔疾病） | 99.53% | L2 | S2 | Research Question |
| 3 | Laryngotracheitis（喉氣管炎） | 99.51% | L5 | S0 | Hold |
| 4 | Tracheal disease（氣管疾病） | 99.49% | L3 | S1 | Research Question |
| 5 | Obstructive lung disease（阻塞性肺病） | 99.48% | **L1** | S3 | **Proceed with Guardrails** |

| 項目 | 內容 |
|---|---|
| 原適應症 | 資料缺口（香港未上市，無核准許可證可查） |
| 作用機轉 (MOA) | 資料缺口 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 安全性初評狀態 | **受阻（Blocking）**——缺 TFDA 仿單警語/禁忌，無法進入 S1 |

---

## 為什麼這些預測合理？

目前缺乏 DrugBank 結構化的作用機轉資料，但從各適應症的文獻共識可還原茶鹼藥理：茶鹼是**非選擇性磷酸二酯酶 (PDE3/4) 抑制劑**及**腺苷受體拮抗劑**，可提升細胞內 cAMP、鬆弛平滑肌（支氣管、氣管），並具低劑量抗發炎/免疫調節效果。

- **阻塞性肺病**：此為茶鹼的經典機轉直接對應，數十年臨床實證（COPD/氣喘）支持，屬於「舊藥適應症再確認」而非真正新預測。
- **氣管疾病 / 鼻腔疾病**：同一 PDE 抑制/腺苷拮抗機轉可外推至氣管平滑肌鬆弛及鼻黏膜抗發炎，NCT03990766（鼻腔灌洗治嗅覺障礙）與早產兒拔管預防性 methylxanthine 使用提供部分人體證據，但樣本量小或非直接治療該疾病本身。
- **血栓性疾病 / 喉氣管炎**：僅為 cAMP 提升→血小板抑制的理論外推或支氣管鬆弛機轉的類比外推，19 篇文獻中無一篇針對茶鹼於血栓疾病之臨床觀察，喉氣管炎則完全無實證支持，判定為知識圖譜共現雜訊。

---

## 各適應症證據明細

### 1. Obstructive Lung Disease（L1，Proceed with Guardrails）

**臨床試驗（前 10 筆，以茶鹼為直接介入藥物者優先）**

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---|---|---|---|---|
| [NCT00252785](https://clinicaltrials.gov/study/NCT00252785) | Phase 3 | 完成 | 340 | Symbicort vs Pulmicort+Theolong(茶鹼)於日本氣喘患者之療效比較 |
| [NCT02261727](https://clinicaltrials.gov/study/NCT02261727) | Phase 4 | 完成 | 1670 | TASCS 試驗：低劑量茶鹼±口服 prednisone 對 COPD 急性惡化之影響 |
| [NCT03984188](https://clinicaltrials.gov/study/NCT03984188) | Phase 3 | 完成 | 100 | 低劑量茶鹼用於生質燃料相關 COPD 之療效 |
| [NCT00756418](https://clinicaltrials.gov/study/NCT00756418) | Phase 4 | 完成 | 84 | Montelukast vs 茶鹼於兒童氣喘加用吸入性類固醇之安全性/療效比較 |
| [NCT00299858](https://clinicaltrials.gov/study/NCT00299858) | Phase 2/3 | 完成 | 24 | 茶鹼對已用長效支氣管擴張劑之 COPD 患者運動耐受力與肺功能之影響 |
| [NCT01132781](https://clinicaltrials.gov/study/NCT01132781) | Phase 2 | 完成 | 28 | 茶鹼於過敏性鼻炎患者之療效 |
| [NCT00241631](https://clinicaltrials.gov/study/NCT00241631) | Phase 2 | 完成 | 49 | 茶鹼+Fluticasone 對 COPD 誘導痰細胞之體外糖皮質激素功能增強作用 |
| [NCT00893009](https://clinicaltrials.gov/study/NCT00893009) | N/A | 未知 | 30 | 茶鹼作為 HDAC 誘導劑對中重度 COPD 小氣道之效果 |
| [NCT02340520](https://clinicaltrials.gov/study/NCT02340520) | Phase 3 | 完成 | 13 | 茶鹼與 Roflumilast 對 COPD 類固醇功能之增強作用 |
| [NCT00671151](https://clinicaltrials.gov/study/NCT00671151) | N/A | 完成 | 35 | 低劑量茶鹼對 COPD 急性惡化分子機轉（NF-κB/HDAC）之調節 |

**文獻（前 10 筆）**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|---|---|---|---|---|
| [1729064](https://pubmed.ncbi.nlm.nih.gov/1729064/) | 1992 | RCT | Chest | 茶鹼與 salbutamol 改善不可逆 COPD 患者肺功能 |
| [3534060](https://pubmed.ncbi.nlm.nih.gov/3534060/) | 1986 | Cohort | J Allergy Clin Immunol | 茶鹼改善 COPD 整體心臟功能並減輕呼吸困難 |
| [8518774](https://pubmed.ncbi.nlm.nih.gov/8518774/) | 1993 | Cohort | Monaldi Arch Chest Dis | 茶鹼改善 COPD 過度充氣與氣體滯留 |
| [23672674](https://pubmed.ncbi.nlm.nih.gov/23672674/) | 2013 | Review | Am J Respir Crit Care Med | Barnes 茶鹼機轉綜述：低劑量抗發炎效果 |
| [9756187](https://pubmed.ncbi.nlm.nih.gov/9756187/) | 1998 | Review | Clin Exp Allergy | 茶鹼於 COPD 之抗發炎/免疫調節活性 |
| [8214921](https://pubmed.ncbi.nlm.nih.gov/8214921/) | 1993 | RCT | Am Rev Respir Dis | 茶鹼改善嚴重 COPD 休息/運動/睡眠時氣體交換 |
| [2877017](https://pubmed.ncbi.nlm.nih.gov/2877017/) | 1986 | Review | J Allergy Clin Immunol | 茶鹼於 COPD 維持治療之角色 |
| [8513541](https://pubmed.ncbi.nlm.nih.gov/8513541/) | 1993 | Review | Cleve Clin J Med | 解決茶鹼於 COPD 門診治療爭議 |
| [14988770](https://pubmed.ncbi.nlm.nih.gov/14988770/) | 2004 | Review | Drugs of Today | 茶鹼機轉與其於氣喘/COPD 之應用 |
| [27844172](https://pubmed.ncbi.nlm.nih.gov/27844172/) | 2017 | Review | Handb Exp Pharmacol | 黃嘌呤類與 PDE 抑制劑總論 |

### 2. Nasal Cavity Disease（L2，Research Question）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---|---|---|---|---|
| [NCT03990766](https://clinicaltrials.gov/study/NCT03990766) | Phase 2 | 完成 | 27 | SCENT 試驗：鼻腔茶鹼灌洗治療病毒後嗅覺障礙，樣本小但為唯一直接人體介入試驗 |

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|---|---|---|---|---|
| [9648963](https://pubmed.ncbi.nlm.nih.gov/9648963/) | 1998 | RCT | Eur Respir J | 緩釋茶鹼減弱過敏性鼻炎患者鼻抗原刺激後的嗜酸性球發炎反應 |
| [21139231](https://pubmed.ncbi.nlm.nih.gov/21139231/) | 2010 | Animal model | Biol Pharm Bull | 天竺鼠氣喘模型中鼻腔為過敏原進入路徑（機轉背景） |
| [11331690](https://pubmed.ncbi.nlm.nih.gov/11331690/) | 2001 | Cohort | Pediatrics | 高流量鼻導管裝置研究，與茶鹼無直接關聯，僅供背景參考 |

### 3. Tracheal Disease（L3，Research Question）

無臨床試驗登記。文獻多為離體/動物氣管平滑肌鬆弛研究（茶鹼常作為陽性對照組），人類證據侷限於早產兒拔管預防性 methylxanthine 使用：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|---|---|---|---|---|
| [10796303](https://pubmed.ncbi.nlm.nih.gov/10796303/) | 2000 | SR/Meta-analysis | Cochrane Database Syst Rev | Methylxanthine 預防性用於早產兒拔管 |
| [12535389](https://pubmed.ncbi.nlm.nih.gov/12535389/) | 2003 | SR/Meta-analysis | Cochrane Database Syst Rev | 同上，更新版 |
| [2353933](https://pubmed.ncbi.nlm.nih.gov/2353933/) | 1990 | Preclinical | Biochem Pharmacol | 咖啡因/茶鹼/enprofylline 類似物之氣管鬆弛活性 |
| [27334733](https://pubmed.ncbi.nlm.nih.gov/27334733/) | 2016 | Animal model | Adv Exp Med Biol | 茶鹼於卵白蛋白誘發過敏發炎模型之支氣管擴張/抗發炎作用 |
| [31565900](https://pubmed.ncbi.nlm.nih.gov/31565900/) | 2019 | Retrospective (獸醫) | J Vet Sci | 茶鹼治療小型犬氣管塌陷之回溯性研究 |
| [26456328](https://pubmed.ncbi.nlm.nih.gov/26456328/) | 2015 | Review | J Ethnopharmacol | 藥用植物對氣管平滑肌鬆弛效果綜述（茶鹼為對照） |
| [1896248](https://pubmed.ncbi.nlm.nih.gov/1896248/) | 1991 | Preclinical | Pediatr Res | 茶鹼與咖啡因對早產羊氣管平滑肌作用之區隔 |
| [3240706](https://pubmed.ncbi.nlm.nih.gov/3240706/) | 1988 | Preclinical | Drugs Exp Clin Res | Doxofylline 與茶鹼作用機轉部分不同之比較 |
| [16397917](https://pubmed.ncbi.nlm.nih.gov/16397917/) | 2006 | Preclinical | Phytother Res | Thymus vulgaris 對氣管鬆弛效果（茶鹼為陽性對照） |
| [17034662](https://pubmed.ncbi.nlm.nih.gov/17034662/) | 2006 | Preclinical | J Pharm Pharmacol | 番紅花萃取物氣管鬆弛效果（茶鹼為陽性對照） |

### 4. Thrombotic Disease（L5，Hold）

目前無相關臨床試驗登記。19 篇文獻中僅少數提及茶鹼，且皆非直接臨床觀察，多為血小板生物標記方法學或無關藥物（如 ticlopidine）之藥動學研究：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|---|---|---|---|---|
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Basic/Assay | Br J Haematol | 血小板因子 4 放射免疫測定法，茶鹼僅作為抗凝血劑成分之一 |
| [6241135](https://pubmed.ncbi.nlm.nih.gov/6241135/) | 1984 | Cohort | Cor et Vasa | 血管疾病患者「茶鹼抗性 T 細胞」比例上升（非治療性研究） |
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | Pharmacology | Gen Pharmacol | Milrinone 與腺苷對血小板反應之交互作用（cAMP 機轉相關背景） |
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Review/PK | Clin Pharmacokinet | Ticlopidine 之臨床藥動學（與茶鹼無關） |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Review | CRC Crit Rev Biochem | Prostaglandin/血小板/動脈粥狀硬化綜述（背景機轉） |

其餘文獻（血小板-白血球聚集、microRNA 訊號、C 型凝集素受體檢測法等）與茶鹼於血栓疾病之直接治療關聯性更低，予以省略以避免誤導。

### 5. Laryngotracheitis（L5，Hold）

目前無相關臨床試驗登記。目前無相關文獻。

---

## 香港上市資訊

目前於香港無核准許可證（未上市，`total_licenses = 0`）。

---

## 安全性考量

安全性資訊請參考原廠仿單。（TFDA 仿單警語/禁忌、DDI 資料均為缺口，且此缺口已被標記為 **Blocking**，直接阻斷 S1 安全性初評階段。）

---

## 結論與下一步

**整體決策：Hold（待補關鍵資料）** — 唯一達 L1 等級的「Obstructive Lung Disease」雖可標記 **Proceed with Guardrails**，但因仿單警語/禁忌資料缺口為 Blocking severity，**任一適應症皆無法正式進入 S1 安全性初評**，故現階段整包建議暫緩，先補資料缺口。

**理由：**
- 阻塞性肺病證據充分（多項 Phase 3/4 RCT），但屬既有用途再確認而非新機會；其餘 4 項預測證據薄弱（L2–L5），多為機轉外推或 KG 共現雜訊。
- DG001（TFDA/衛生署仿單警語與禁忌缺失，Blocking）是所有候選適應症共同的硬性阻斷點。

**若要推進需要：**
1. 補齊 DG001：取得原廠仿單或香港衛生署核准資料，解析警語與禁忌 → 解除 S1 阻斷。
2. 補齊 DG002：向 DrugBank API 查詢完整 MOA，強化機轉關聯性分析。
3. 針對「鼻腔疾病」「氣管疾病」設計前瞻性小型概念驗證試驗，將現有動物/離體證據轉化為人體證據。
4. 「血栓性疾病」「喉氣管炎」因證據等級過低且屬 KG 雜訊，暫不建議投入資源，除非未來出現新的直接證據。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

