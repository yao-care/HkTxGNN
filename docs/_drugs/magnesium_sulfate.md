---
layout: default
title: Magnesium Sulfate
parent: 高證據等級 (L1-L2)
nav_order: 471
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

# Magnesium Sulfate：從資料缺口到子癲前症/子癲症（實為既有標準治療再確認）

## 一句話總結

Magnesium Sulfate（硫酸鎂）原適應症資料在本評估包中為缺口（Data Gap），但作為藥物本身，硫酸鎂數十年來即為國際公認的子癲前症/子癲症抗痙攣標準治療。
TxGNN 模型將其最高分預測指向**子癲前症/子癲症 (Preeclampsia/Eclampsia)**（預測分數 99.9992%），
但證據回顧顯示這實質上是「既有標準治療的再確認」而非典型的老藥新用候選，目前有 **50 個臨床試驗登記**與 **20 篇文獻**支持此一用途，其中至少 2 個已完成的 Phase 3 RCT。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | ⚠ 資料缺口（DG001/DG002，見下方說明）；已知為國際標準抗痙攣治療 |
| 預測新適應症 | 子癲前症/子癲症 (Preeclampsia/Eclampsia) |
| TxGNN 預測分數 | 99.9992%（rank 48） |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails（惟需先釐清是否屬既有適應症，見下方說明） |

---

## 為什麼這個預測合理？

硫酸鎂的作用機轉為：抑制 NMDA 受體、降低神經肌肉接合處的興奮性傳導，並擴張腦血管以緩解腦血管痙攣，三者共同產生抗痙攣效果。這是子癲前症/子癲症抽搐預防與治療數十年來的核心藥理基礎，也是 WHO 與 ACOG 指引中的第一線用藥。

TxGNN 將「toxemia of pregnancy」（妊娠毒血症，子癲前症/子癲症的舊稱）獨立列為第二高分預測（99.9984%），兩者實為同一臨床實體在知識圖譜中被拆分成兩個疾病節點，證據體高度重疊，並非兩個獨立的新適應症。

**重要提醒**：本評估包的 `original_indications` 欄位為空、`original_moa` 標示為 Data Gap，屬於資料庫收錄缺口，而非代表硫酸鎂尚未核准用於子癲前症/子癲症。換言之，TxGNN 在這裡預測出的「新適應症」很可能只是補上了資料庫遺漏的既有適應症，建議在後續決策前先確認並補齊 DG001（仿單警語/禁忌）與 DG002（正式 MOA 收錄），把焦點放在劑量優化與特殊族群（如肥胖、產後延長使用）而非新適應症開發。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03318211](https://clinicaltrials.gov/study/NCT03318211) | Phase 4 | 未知 | 100 | 重度子癲前症產後是否持續使用硫酸鎂之隨機對照試驗 |
| [NCT02835339](https://clinicaltrials.gov/study/NCT02835339) | Phase 4 | 完成 | 66 | 肥胖子癲前症孕婦之硫酸鎂藥動學與劑量調整研究 |
| [NCT01846156](https://clinicaltrials.gov/study/NCT01846156) | Phase 3 | 完成 | 240 | 比較不同硫酸鎂給藥方案於重度子癲前症之最佳化 |
| [NCT03164304](https://clinicaltrials.gov/study/NCT03164304) | Phase 4 | 完成 | 222 | 1g vs 2g IV 維持劑量之療效與安全性比較 |
| [NCT02091401](https://clinicaltrials.gov/study/NCT02091401) | Phase 4 | 完成 | 200 | Springfusor 間歇 bolus 給藥 vs 連續輸注之血中鎂濃度等效性 |
| [NCT01492608](https://clinicaltrials.gov/study/NCT01492608) | Phase 3 | 完成 | 560 | MASP-STUDY：早產兒硫酸鎂神經保護以預防腦性麻痺 |
| [NCT02307201](https://clinicaltrials.gov/study/NCT02307201) | Phase 2/3 | 完成 | 1114 | 產前已用藥 ≥8 小時者，產後是否需再維持 24 小時硫酸鎂 |
| [NCT02317146](https://clinicaltrials.gov/study/NCT02317146) | Phase 2/3 | 完成 | 280 | 產前用藥 <8 小時者，產後 6 小時 vs 24 小時方案比較 |
| [NCT01911494](https://clinicaltrials.gov/study/NCT01911494) | N/A | 完成 | 87500 | CLIP 大型社區介入試驗，改善妊娠高血壓疾病之整體照護 |
| [NCT00004399](https://clinicaltrials.gov/study/NCT00004399) | N/A | 完成 | 2000 | Nimodipine vs 硫酸鎂預防重度子癲前症抽搐之經典大型試驗 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [9794688](https://pubmed.ncbi.nlm.nih.gov/9794688/) | 1998 | Review | Obstetrics and Gynecology | 回顧硫酸鎂用於子癲前症/子癲症抽搐預防之療效、益處與風險 |
| [2288560](https://pubmed.ncbi.nlm.nih.gov/2288560/) | 1990 | Review | American Journal of Obstetrics and Gynecology | 硫酸鎂為子癲前症/子癲症之理想抗痙攣藥物，療效安全性已有60年文獻佐證 |
| [39110688](https://pubmed.ncbi.nlm.nih.gov/39110688/) | 2024 | Cohort（質性研究） | PLoS One | 坦尚尼亞助產士對硫酸鎂使用之認知與劑量/毒性評估落差 |
| [2672428](https://pubmed.ncbi.nlm.nih.gov/2672428/) | 1989 | — | Stroke | 硫酸鎂透過拮抗鈣依賴性血管收縮緩解腦血管痙攣之機轉研究 |
| [16978425](https://pubmed.ncbi.nlm.nih.gov/16978425/) | 2006 | — | Obstetrical & Gynecological Survey | 子癲前症腦血流動力學回顧，探討硫酸鎂以外替代方案之理論基礎 |
| [41054655](https://pubmed.ncbi.nlm.nih.gov/41054655/) | 2025 | — | Cureus | 硫酸鎂於兒科急診（重度氣喘、頑固性癲癇、心律不整）應用回顧 |
| [31527059](https://pubmed.ncbi.nlm.nih.gov/31527059/) | 2019 | — | Global Health, Science and Practice | 資源有限地區推行硫酸鎂預防子癲症需仰賴完整醫療系統支持 |
| [25353716](https://pubmed.ncbi.nlm.nih.gov/25353716/) | 2015 | — | Acta Obstetricia et Gynecologica Scandinavica | 低收入國家降低子癲前症/子癲症相關孕產婦死亡之介入評估 |
| [23282276](https://pubmed.ncbi.nlm.nih.gov/23282276/) | 2012 | — | Rev Med Inst Mex Seguro Soc | 墨西哥子癲前症/子癲症臨床指引 |
| [36413336](https://pubmed.ncbi.nlm.nih.gov/36413336/) | 2023 | — | Biological Trace Element Research | 硫酸鎂治療下重度子癲前症患者發生急性高鎂血症之發生率與風險因子 |

---

## 香港上市資訊

目前 Magnesium Sulfate 於香港無有效藥品許可證登記（`market_status: 未上市`，`total_licenses: 0`），無法提供品名／劑型／核准適應症等細節。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠ 資料缺口提醒：TFDA/香港仿單警語與禁忌症（DG001，Blocking）與正式 MOA 收錄（DG002，High）均尚未取得，前者直接影響是否能進入 S1 安全性初評，建議優先補齊。

---

## 補充：其他 TxGNN 預測候選（rank 2-5）

| 排名 | 疾病 | 分數 | 證據等級 | 決策階段 | 建議 | 備註 |
|------|------|------|---------|---------|------|------|
| 2 | Toxemia of pregnancy | 99.9984% | L1 | S3 | Proceed with Guardrails | 與 rank 1 為同一臨床實體（子癲前症/子癲症舊稱），非獨立新適應症 |
| 3 | Thrombotic disease | 99.90% | L2 | S2 | Research Question | 直接證據（MAGMAT RCT）僅限「血栓性血小板減少性紫斑症(TTP)」亞型，非廣泛血栓疾病 |
| 4 | Pharyngitis | 99.61% | L2 | S1 | Research Question | 證據實為「插管相關術後喉嚨痛」，與傳統感染/發炎性咽炎定義錯位，需先確認 TxGNN 疾病節點映射是否正確 |
| 5 | Nasal cavity disease | 99.59% | L5 | S0 | Hold | 無任何機轉或臨床證據支持，唯一收錄試驗與鼻腔疾病無關，純屬模型關聯推論 |

---

## 結論與下一步

**決策：Proceed with Guardrails**（僅適用於 rank 1「子癲前症/子癲症」）

**理由：**
- 有多個已完成的 Phase 2/3/4 RCT（含大型社區介入試驗 CLIP, n=87500）支持硫酸鎂於子癲前症/子癲症之療效，證據等級達 L1。
- 但 `original_indications` 空白很可能是資料庫收錄缺口，而非此藥真的尚未核准此用途——建議先確認再決定是否以「老藥新用」流程處理，或改列為既有適應症之劑量/安全性優化專案。
- Rank 3（血栓/TTP）證據品質尚可但需限縮適應症範圍；Rank 4（咽炎）疾病標籤與實際證據錯位；Rank 5（鼻腔疾病）無實質證據支持，應標記 Hold。

**若要推進需要：**
- 補齊 DG001（TFDA/香港仿單警語與禁忌，Blocking）與 DG002（正式 MOA 收錄，High）
- 確認硫酸鎂是否本就已核准用於子癲前症/子癲症，釐清此候選的真實定位（既有適應症資料補正 vs. 真正新適應症）
- 若確定香港未上市，需評估在地上市申請路徑與監管要求
- 對 rank 3（thrombotic disease）建議將目標適應症限縮為 TTP 並持續追蹤 MAGMAT 試驗最終結果
- 對 rank 4、5 暫緩投入資源，待疾病節點映射與證據品質問題釐清後再評估
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

